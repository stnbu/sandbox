#!/bin/sh -ue

# ./this_script.sh <org_file_name> <dapps_url_relative_path>

if [ "${1-}" = "" ] ; then
    SRC=/home/mburr/git/sandbox/all.org
    DST=/var/www/dapps.unintuitive.org/index.html
else
    SRC=$1
    DST=$1
fi

emacs "$SRC" --batch -f org-html-export-to-html --kill >/dev/null 2>&1
OUTPUT_FILE_NAME=$(echo "$SRC" | sed 's/\(.*\.\)org$/\1html/')
mv "$OUTPUT_FILE_NAME" "$DST"
echo -n "Happy!"
