import fire
import subprocess
from pathlib import Path
import os
from fire.core import Display
import pydoc

# Disable pager globally
#pydoc.pager = print


os.environ['HLBFX_NFS_DIR'] = "/nfs/team298/projects"
os.environ['HLBFX_LUSTRE_DIR'] = "/lustre/scratch126/cellgen/haniffa/projects/"
os.environ['HLBFX_USER_DIR'] = f"/nfs/team298/{os.environ['USER']}/projects"
SCRIPT_DIR = Path(__file__).parent/"scripts"


class Project:
    
    #def help(self):
    #    """Manually show help"""
    #    display = Display()
    #    help_str = display.GetFormatHelp(Project)
    #    print(help_str, file=sys.stderr)


    def ls(self):
        """List available projects"""
        results = subprocess.run(["bash", str(SCRIPT_DIR / "ls.sh")], check=True)
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

        results = subprocess.run(["bash", str(SCRIPT_DIR / "create.sh"), name],
                                 check=True) #, capture_output = True, shell=True)
        return results.stdout

    def add(self, name: str):
        """Add something to an existing project"""
        if not name:
            raise ValueError("Project name must be provided")
        if not isinstance(name, str):
            raise TypeError("Project name must be a string")

        results = subprocess.run(["bash", str(SCRIPT_DIR / "add.sh"), name],
                                 check=True) #, capture_output = True, shell=True)
        return results.stdout

def main():
    """Main function to run the CLI"""
    fire.Fire(Project, name="hlbfx-project")

if __name__ == "__main__":
    main()
