# from manim import *

# class DiscontinuousExample(Scene):
#     def construct(self):
#         ax1 = NumberPlane((-3, 3), (-4, 4))
#         ax2 = NumberPlane((-3, 3), (-4, 4))
#         VGroup(ax1, ax2).arrange()
#         discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
#         incorrect = ax1.plot(discontinuous_function, color=RED)
#         correct = ax2.plot(
#             discontinuous_function,
#             discontinuities=[-2, 2],  # discontinuous points
#             dt=0.1,  # left and right tolerance of discontinuity
#             color=GREEN,
#         )
#         self.add(ax1, ax2, incorrect, correct)


# """
# # Elliptic curve parameters A and B of the curve : y² = x³ Ax + B
# A: int = 0
# B: int = 7
# """


# def xec(x):
#     return math.sqrt(x)
#     before_sqrt = x**3 + 7
#     if before_sqrt < 0.0:
#         return 0.0
#     return math.sqrt(before_sqrt)
            ##lambda x, y: x * y ** 2 - x ** 2 * y - 2,

import math
from manim import *

config.frame_height = 8 * 3
config.frame_width = config.frame_height * config.aspect_ratio
config.quality = "low_quality"

class EC(Scene):
    def construct(self):
        extent = 1000
        plane = NumberPlane((-extent, extent), (-extent, extent))
        graph = ImplicitFunction(
            lambda x, y: x**3 + 7 - y**2,
            color=YELLOW
        )
        self.add(plane, graph)