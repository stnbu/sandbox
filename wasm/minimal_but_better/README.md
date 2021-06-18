Maybe `--reference-types`? (only Firefox 79+ and Chrome)

```
cargo build --target wasm32-unknown-unknown
wasm-bindgen --out-dir pkg --target web --reference-types --no-typescript --omit-default-module-path target/wasm32-unknown-unknown/debug/minimal_but_better.wasm
```

Hmm. This happens in Chrome `91.0.4472.106 (Official Build) (x86_64)` but works in Firefox `89.0.1 (64-bit)`...

```
Uncaught (in promise) CompileError: WebAssembly.instantiateStreaming(): invalid value type 'externref', enable with --experimental-wasm-reftypes @+25
```
