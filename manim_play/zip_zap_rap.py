from manim import *
from decimal import Decimal

from pprint import pprint

class W(Scene):
    def construct(self):
        modulus = 10
        axis_config = {}  #{"scaling": WrappedScale(Decimal(modulus))}
        t_range = [-10, 10, 1]
        #import ipdb; ipdb.set_trace()
        ax = Axes(
            x_range=t_range,
            y_range=t_range,
            x_length=13,
            y_length=13,
            #x_axis_config=axis_config,
            #y_axis_config=axis_config
        )#.add_coordinates()

        self.add(ax)

        modulus = Decimal(10)
        lines = []
        m = 100
        points = []
        for n in range(int(0.01*m), int(30*m), int(0.2*m)):
            x = n / 100
            y = x ** 2

            if len(points) > 1 and y > modulus:
                points.append((x, float(modulus)))
                lines.append(points)
                points = [(x, 0)]

            points.append((
                    x,
                    float(Decimal(y) % modulus)
            ))

        #pprint(lines)

        for line in lines:
            #import ipdb; ipdb.set_trace()
            start = Circle(radius=0.2, color=RED, fill_opacity=1).move_to(ax.coords_to_point(*line[0]))
            end = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to(ax.coords_to_point(*line[-1]))
            self.add(start, end)
            vline = VGroup(color=BLUE)
            vertices = [ax.coords_to_point(x, y) for x, y in line]
            vline.set_points(vertices)
            self.add(vline)

if __name__ == "__main__":
    #import ipdb; ipdb.set_trace()
    config.quality = "low_quality"
    #config.aspect_ratio = 1
    config.frame_height = 15
    config.frame_width = 15
    scene = W()
    scene.render()
