#!/usr/bin/env python3

base_height = 22
base_width = 22

from manim import *

config.frame_height = base_height
config.frame_width = base_width
config.pixel_width = 1024
config.pixel_height = 1024 * 2

class Ax(Scene):

    def construct(self):
        extent = base_height / 2
        plane = Axes(
            x_range=[-1 , extent - 1, 1],
            y_range=[1 - extent, extent - 1, 1],
            y_length=base_width * 1.5,
            tips=False,
            axis_config={"include_numbers": True},
        )
        self.add(plane)

if __name__ == "__main__":
    scene = Ax()
    scene.render()
