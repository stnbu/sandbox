from manim import *

class D(Scene):
    def construct(self):
        plane = Axes().add_coordinates()

        # a dot with respect to the axes
        dot = Dot(plane.coords_to_point(2, 2), color=GREEN)
        #lines = plane.get_lines_to_point(plane.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        #plane = NumberPlane()
        #dot_scene = Dot((2,2,0), color=RED)

        self.add(plane, dot)
