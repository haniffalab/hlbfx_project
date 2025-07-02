#!/bin/bash


if [ $# -ne 1 ]; then
  echo "Usage: $0 <project_name>"
  exit 1
fi




project_name=$1; shift

warn() {
  echo -e "\033[1;33m[WARNING]\033[0m $1"
}

error() {
  echo -e "\033[1;31m[ERROR]\033[0m $1"
}

success() {
  echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}



BACKUP_BASE=$HLBFX_NFS_DIR
backup_dir=$BACKUP_BASE/$project_name

NOBACKUP_BASE=$HLBFX_LUSTRE_DIR
nobackup_dir=$NOBACKUP_BASE/$project_name

USER_DIR=$HLBFX_USER_DIR
user_dir=$USER_DIR/$project_name

backup_dir_present=0
if [ -d "$backup_dir" ]; then
  error "Directory $backup_dir already exists in $BACKUP_BASE"
  backup_dir_present=1
fi

nobackup_dir_present=0
if [ -d "$nobackup_dir" ]; then
  error "Directory $nobackup_dir already exists in $NOBACKUP_BASE"
  nobackup_dir_present=1
fi
user_dir_present=0
if [ -d "$user_dir" ]; then
  error "Directory $user_dir already exists in $USER_DIR"
  user_dir_present=1
fi

if [ $backup_dir_present -eq 1 ] || [ $nobackup_dir_present -eq 1 ] || [ $user_dir_present -eq 1 ]; then
  error "Project creation aborted due to existing directories."
  exit 0
fi


# Create the backup and nobackup directories
mkdir -p $backup_dir
mkdir -p $nobackup_dir
mkdir -p $user_dir

# Create the project directory structure
mkdir -p $user_dir/{codes/$USER,freeze/codes/,envs/$USER,intermediate_data}
mkdir -p $backup_dir/{freeze_data,results}
mkdir -p $nobackup_dir/{nobackup_data,nobackup_output,tmp}
touch $backup_dir/README.md

# Create softlinks
ln -s $backup_dir/freeze_data $user_dir/freeze/data
ln -s $backup_dir/results/ $user_dir/results
ln -s $nobackup_dir/{nobackup_data,nobackup_output} $user_dir/intermediate_data
ln -s $nobackup_dir/tmp $user_dir/tmp

echo "Project $project_name " > $backup_dir/README.md
cp $backup_dir/README.md $user_dir/README.md

chmod -R 774 $backup_dir $nobackup_dir $user_dir
echo "Your project folder is $user_dir"
