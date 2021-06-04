#!/bin/sh -ue

# ./this_script.sh <org_file_name> <dapps_url_relative_path>

emacs "$1" --batch -f org-html-export-to-html --kill >/dev/null 2>&1
OUTPUT_FILE_NAME=$(echo "$1" | sed 's/\(.*\.\)org$/\1html/')
# we are depending on -e here
mv "$OUTPUT_FILE_NAME" /var/www/dapps.unintuitive.org/"$2"
