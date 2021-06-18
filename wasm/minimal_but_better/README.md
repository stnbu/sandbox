Maybe `--reference-types`?

```
cargo build --target wasm32-unknown-unknown
wasm-bindgen --out-dir pkg --target web --no-typescript --omit-default-module-path target/wasm32-unknown-unknown/debug/minimal_but_better.wasm
```
