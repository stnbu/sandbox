#!/bin/sh -ue

DEST="$1"
mkdir -p "$DEST" # wasm-bindgen will do this, but this makes it easy to find the "cargo root"

cd "$DEST"
while true ; do
    test -e "./Cargo.toml" && break
    cd ..
done

CRATE_NAME=$(grep -E 'name[ ]*=' Cargo.toml | sed -E 's/.*=.*"(.*)"/\1/') # yuu
CRATE_NAME=$(echo $CRATE_NAME | sed 's/-/_/g')                            # uck

cargo build --target wasm32-unknown-unknown
wasm-bindgen --out-dir "${DEST}" --target web --reference-types --no-typescript \
	     --omit-default-module-path \
	     target/wasm32-unknown-unknown/debug/"${CRATE_NAME}".wasm
