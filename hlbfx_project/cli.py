import fire
import subprocess
from pathlib import Path
import os
import sys
from fire.core import Display
import pydoc

import inspect
#print(inspect.__file__)
# Disable pager globally
#pydoc.pager = print


os.environ.setdefault("HLBFX_NFS_DIR", "/nfs/team298/projects")
os.environ.setdefault("HLBFX_LUSTRE_DIR", "/lustre/scratch124/cellgen/haniffa/projects/")
os.environ.setdefault("HLBFX_USER_DIR", f"/nfs/team298/{os.environ['USER']}/projects")


def _candidate_script_dirs() -> list[Path]:
    candidates: list[Path] = []

    override = os.environ.get("HLBFX_PROJECT_SCRIPTS_DIR")
    if override:
        candidates.append(Path(override).expanduser().resolve())

    candidates.append((Path(__file__).resolve().parent / "scripts"))

    exe_dir = Path(sys.argv[0]).resolve().parent
    env_root = exe_dir.parent
    site_packages_roots = list((env_root / "lib").glob("python*/site-packages"))
    for root in site_packages_roots:
        candidates.append(root / "hlbfx_project" / "scripts")

    project_root_candidate = (Path.cwd() / "hlbfx_project" / "scripts").resolve()
    candidates.append(project_root_candidate)

    # Preserve order while removing duplicates.
    unique: list[Path] = []
    seen: set[Path] = set()
    for c in candidates:
        if c not in seen:
            seen.add(c)
            unique.append(c)
    return unique


def _script_path(script_name: str) -> Path:
    for script_dir in _candidate_script_dirs():
        candidate = script_dir / script_name
        if candidate.is_file():
            return candidate

    searched = "\n".join(str(p) for p in _candidate_script_dirs())
    raise FileNotFoundError(
        f"Could not find {script_name}. Looked in:\n{searched}\n"
        "Set HLBFX_PROJECT_SCRIPTS_DIR to the directory containing the shell scripts."
    )


class Project:
    
    #def help(self):
    #    """Manually show help"""
    #    display = Display()
    #    help_str = display.GetFormatHelp(Project)
    #    print(help_str, file=sys.stderr)


    def ls(self):
        """List available projects"""
        results = subprocess.run(["bash", str(_script_path("ls.sh"))], check=True)
        return results.stdout

    def create(self, name: str):
        """
        Create a new project

        DO NOT use spaces in the project name or special characters such as +,
        ? !, @, #, $, %, ^, &, *, (, ), etc.

        Args:
            name (str): Name of the new project
        """
        if not name:
            raise ValueError("Project name must be provided")
        if not isinstance(name, str):
            raise TypeError("Project name must be a string")

        results = subprocess.run(["bash", str(_script_path("create.sh")), name],
                                 check=True) #, capture_output = True, shell=True)
        return results.stdout

    def add(self, name: str):
        """Add something to an existing project"""
        if not name:
            raise ValueError("Project name must be provided")
        if not isinstance(name, str):
            raise TypeError("Project name must be a string")

        results = subprocess.run(["bash", str(_script_path("add.sh")), name],
                                 check=True) #, capture_output = True, shell=True)
        return results.stdout

def main():
    """Main function to run the CLI"""
    fire.Fire(Project, name="hlbfx-project")

if __name__ == "__main__":
    main()
