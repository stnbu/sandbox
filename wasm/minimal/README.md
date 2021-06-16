# _Minimal_ example of deploying wasm without a "bundler"

This is just a ripoff of [this](), but there's so much stuff to keep up with, I wanted an ultra-minimal example, since with this "stack", it seems like things break if you breath on them wrong. If it's useful to you, great!

1. Get `wasm-pack` installed and run `wasm-pack build --target web` in the directory containing this README file.
1. Somehow serve the directory containing `index.html` on a web server.

Open some developer tools to see what's going on at least look at the JavaScript console output. For me, opening `index.html` from the filesystem in my web browser does not work because of cross-origin something-something.

Enjoy lots of great documentation about Rust -vs- WASM [here](https://rustwasm.github.io/docs/book/). That's a good anchor point that links to important stuff and explains everything well (pre-req: some Rust).
