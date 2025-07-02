echo "Listing all projects..."
#ls -1 $HLBFX_NFS_DIR | sort
#ls -1 $HLBFX_NFS_DIR | sort
#stat --format '%n  %U  %y' $HLBFX_NFS_DIR/* | awk  'OFS="\t" {print $1, $2, $3}' | sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2}).*/\3-\2-\1/'

for f in $HLBFX_NFS_DIR/* ; do
	b=`basename "$f"`
  printf "%-30s %-10s %s\n" \
    "$b" \
    "$(stat -c %U "$f")" \
    "$(stat -c %y "$f" | awk -v b=$b -F '[- ]' '{printf "%s-%s-%s", $3, $2, substr($1,3)}')" | sort
done

