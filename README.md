# hlbfx-project 
A CLI using to manage Haniffa Lab Bioinformatics projects.

## Information
* If you are unsure of the steps below please contact vm11 for help setting up the project.
* Only proceed if you are familiar with using the command line, git, and python based installations. 

## Installation
### Usage within farm - No installation needed
```bash
echo "
# hlbfx-project
export PYTHONPATH=\$PYTHONPATH:/software/cellgen/team298/shared/deploy/:/software/cellgen/team298/shared/deploy/lib/python3.12/site-packages/
export PATH=/software/cellgen/team298/shared/deploy/bin/:\$PATH
" >> ~/.bashrc
source ~/.bashrc
```
### Usage outside farm - Install using pip
```bash
pip install git+https://github.com/haniffalab/hlbfx_project.git
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

## Where to find the project
Your projects will be in the nfs team directory `/nfs/team298/USERNAME/projects/`. Change `USERNAME` to your username and `<project_name>` to the name of your project.
```bash
cd /nfs/team298/USERNAME/projects/<project_name>
```
