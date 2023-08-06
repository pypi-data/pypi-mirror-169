import pathlib
import itertools
import shutil

from mycfg import meta, const
from mycfg import lib


class Unit:
    def __init__(self, name, cfg):
        self.name = name
        self.cfg = cfg

        self.files = lib.ensure_list(cfg.get("files", []))
        self.preserve_symlinks = cfg.get("preserve-symlinks", "false") == "true"
        self.exclude_files = lib.ensure_list(cfg.get("exclude-files", []))

        self.install_commands = lib.ensure_list(cfg.get("install-command", []))
        self.install_scripts = lib.ensure_list(cfg.get("install-script", []))

        self.save_scripts_pre = lib.ensure_list(cfg.get("save-scripts-pre", []))
        self.save_scripts_post = lib.ensure_list(cfg.get("save-scripts-post", []))

        self.load_scripts_pre = lib.ensure_list(cfg.get("load-scripts-pre", []))
        self.load_scripts_post = lib.ensure_list(cfg.get("load-scripts-post", []))

        self.required_packages = lib.ensure_list(cfg.get("requires-packages", []))

        self.dotfiles_repo = lib.GitRepo(const.MYCFG_CONFIG_DIR)

    def load(self):
        for pkg in self.required_packages:
            if pkg not in meta.get("installed_packages"):
                lib.install_pkg(pkg)
                meta.append("installed_packages", pkg)
        if self.name not in meta.get("installed_units"):
            for cmd in self.install_commands:
                lib.sh(cmd)
            for script in self.install_scripts:
                lib.exec_script(script)
            meta.append("installed_units", self.name)
        for script in self.load_scripts_pre:
            lib.exec_script(script)

        included_or_excluded = []
        for submodule in self.dotfiles_repo.iter_submodules():
            path = const.HOME.joinpath(pathlib.Path(submodule.path).relative_to(pathlib.Path("dotfiles")))
            if any(itertools.chain.from_iterable([[parent in path.parents for parent in const.HOME.glob(glob)] for glob in self.files])):
                if not path.exists():
                    lib.GitRepo.clone_from(submodule.url, path)
                    lib.print_status(repos=1)
                included_or_excluded.append(path)

        for glob in self.files:
            for file_or_dir in const.DOTFILES_SAVE_DIR.glob(glob):
                if file_or_dir in included_or_excluded:
                    continue

                included_or_excluded.append(file_or_dir)
                if any(map(file_or_dir.match, self.exclude_files)):
                    continue

                if file_or_dir.is_dir():
                    shutil.copytree(file_or_dir, const.HOME.joinpath(
                        file_or_dir.relative_to(const.DOTFILES_SAVE_DIR)),
                        symlinks=self.preserve_symlinks, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(*const.IGNORE_PATTERNS))
                else:
                    dst = const.HOME.joinpath(file_or_dir.relative_to(const.DOTFILES_SAVE_DIR))
                    dst.parent.mkdir(exist_ok=True, parents=True)
                    shutil.copy2(file_or_dir, dst)
        for script in self.load_scripts_post:
            lib.exec_script(script)
        meta.save()

    def save(self):

        for script in self.save_scripts_pre:
            lib.exec_script(script)

        glob_files: list[pathlib.Path] = []
        for glob in self.files:
            glob_files.extend([z for z in const.HOME.glob(glob)])

        copy_files: list[pathlib.Path] = []
        git_dirs: list[pathlib.Path] = []

        for file in glob_files:
            if any(map(file.match, self.exclude_files)):
                continue
            if file.is_file():
                copy_files.append(file)
            elif file.is_dir():
                if file.joinpath(".git").is_dir():
                    git_dirs.append(file)
                else:
                    glob_files.extend(file.iterdir())
        repos: list[lib.GitRepo] = []
        for repo_dir in git_dirs:
            repo = lib.GitRepo(repo_dir.absolute())
            origin = repo.get_origin()
            if origin is None:
                copy_files.append(repo_dir)
                continue
            repo.set_origin(origin)
            repos.append(repo)

        for repo in repos:
            submodule_path = str(pathlib.Path("dotfiles").joinpath(repo.path.relative_to(const.HOME)))
            try:
                self.dotfiles_repo.submodule(submodule_path)
            except ValueError:
                self.dotfiles_repo.create_submodule(submodule_path, submodule_path, url=repo.origin.url, branch=repo.active_branch)
                lib.print_status(repos=1)

        for file in copy_files:
            dst = const.DOTFILES_SAVE_DIR.joinpath(file.relative_to(const.HOME))
            if file.is_file():
                dst.parent.mkdir(exist_ok=True, parents=True)
                shutil.copy2(file, dst, follow_symlinks=self.preserve_symlinks)
            else:
                shutil.copytree(file, dst, symlinks=self.preserve_symlinks, dirs_exist_ok=True, ignore=shutil.ignore_patterns(*const.IGNORE_PATTERNS))

        for script in self.save_scripts_post:
            lib.exec_script(script)

