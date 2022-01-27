extern crate piston_window;
extern crate sdl2_window;

use piston_window::*;
use sdl2_window::Sdl2Window;

fn main() {
    let window = WindowSettings::new("title", [512; 2]).build().unwrap();
}
