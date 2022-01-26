#!/usr/bin/env python3

base_height = 22
base_width = 22

from manim import *

config.frame_height = base_height
config.frame_width = base_width
config.pixel_width = 1024
config.pixel_height = 1024 # int(1024 * 1.6)

class Ax(Scene):

    def construct(self):
        extent = base_height / 2
        #import ipdb; ipdb.set_trace()
        x_range = [-1 , extent - 1, 1]
        y_range = [1 - extent, extent - 1, 1]
        plane = Axes(
            x_range=x_range,
            y_range=y_range,
            y_length=(x_range[1] - x_range[0]) * 3,
            tips=False,
            axis_config={"include_numbers": True},
        )
        self.add(plane)
        origin, unit_x, unit_y = self.camera.points_to_pixel_coords(plane, points=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        import ipdb; ipdb.set_trace()

        unit_y = plane.get_vertical_line(plane.coords_to_point(0, 1), color=GREEN, stroke_width=7)
        unit_x = plane.get_horizontal_line(plane.coords_to_point(1, 0), color=BLUE, stroke_width=7)

        
        self.add(unit_x, unit_y)

if __name__ == "__main__":
    scene = Ax()
    scene.render()
