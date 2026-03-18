# hlbfx-project 
A CLI using to manage Haniffa Lab Bioinformatics projects.

## Information
* If you are unsure of the steps below please contact vm11 for help setting up the project.
* Only proceed if you are familiar with using the command line, git, and python based installations. 

## Installation
### Usage within farm - No installation needed
Bug: If you have been using hlbfx-projects before 12/12/2025 please go to your `~/.bashrc` file and remove any previous `hlbfx-projects` PATH additions to avoid conflicts.

```bash
echo "
# hlbfx-project
export PATH=/software/cellgen/team298/shared/hlbfx-projects/bin/:\$PATH
" >> ~/.bashrc
source ~/.bashrc
```
### Usage outside farm - Install using conda and pip
```bash
# Create conda environment per user
conda create -n hlbfx-projects python=3.12 -y
conda activate hlbfx-projects
# Install hlbfx-projects in a common dir for all users
conda create -p /software/cellgen/team298/shared/hlbfx-projects python=3.12 -y
conda activate /software/cellgen/team298/shared/hlbfx-projects
# Install hlbfx-projects in the conda env
git clone git@github.com:haniffalab/hlbfx_project.git
cd hlbfx_project
pip install -e .
# Add hlbfx-projects to your PATH
echo "
# hlbfx-project
export PATH=/software/cellgen/team298/shared/hlbfx-projects/bin/:\$PATH
" >> ~/.bashrc
source ~/.bashrc
```

## Usage

```bash
hlbfx-projects --help
```
### Find if your project is already created
```bash
hlbfx-projects ls
```
### If project does not exist
```bash
hlbfx-projects create <project_name> 
```
### If project exists
```bash
hlbfx-projects add <project_name>
```

## Troubleshooting script path issues
If you see an error where `add.sh`/`create.sh`/`ls.sh` cannot be found from site-packages, point the CLI to the scripts directory explicitly:

```bash
export HLBFX_PROJECT_SCRIPTS_DIR=/path/to/hlbfx_project/scripts
hlbfx-projects add <project_name>
```

Example for this repository clone:

```bash
export HLBFX_PROJECT_SCRIPTS_DIR=$PWD/hlbfx_project/scripts
```

## Where to find the project
Your projects will be in the nfs team directory `/nfs/team298/USERNAME/projects/`. Change `USERNAME` to your username and `<project_name>` to the name of your project.
```bash
cd /nfs/team298/USERNAME/projects/<project_name>
```
