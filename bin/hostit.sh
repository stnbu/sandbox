#!/bin/sh -ue

ME=$(basename $0)
HOST="dapps.unintuitive.org"
REMOTE_PATH="/var/www/dapps.unintuitive.org"

if test $# -ne 2 ; then
    echo "Usage: ${ME} <fromdir> <url_fully_qualified_path>" >&2
    echo " Your content will be hosted at https://${HOST}/<fromdir>" >&2
    echo " trailing a trailing slash for <fromdir> is implied (forced). '.git/' is explicitly omitted." >&2
    exit 1
fi

LOCAL_PATH="$( cd -- "$1" >/dev/null 2>&1 ; pwd -P )"

URL_PATH="$2"  # fixme: catch stupid stuff

cd "$LOCAL_PATH"  # so git stuff works
rsync -v --exclude .git -xa ./ ${HOST}:${REMOTE_PATH}/${URL_PATH}/

# todo: maybe be smart about excluding junk (using 'git check-ignore *' as a lead)
