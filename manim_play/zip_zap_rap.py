from manim import *
from decimal import Decimal

from pprint import pprint

class p:

    modulus = Decimal(10)

    def __init__(self, x, y):
        self.next = None
        self.x = x if isinstance(x, Decimal) else Decimal(x)
        self.y = y if isinstance(y, Decimal) else Decimal(y)
        self.x_remainder = self.x % self.modulus
        self.y_remainder = self.y % self.modulus
        self.x_floor = self.x - self.x_remainder
        self.y_floor = self.y - self.y_remainder
        self.x_muls = self.x_floor // self.modulus
        self.y_muls = self.y_floor // self.modulus

    def get_next(self):
        return self.next

    def get_float_points(self):
        return float(self.x), float(self.y)

class W(Scene):
    def construct(self):
        modulus = 10
        axis_config = {}  #{"scaling": WrappedScale(Decimal(modulus))}
        t_range = [-10, 10, 1]
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
        y_zones = {}
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
    point = p(0, 0)
    root = point
    m = 100
    c = 0
    for n in range(int(0.01*m), int(30*m), int(1.2*m)):
        c += 1
        x = n / 100
        y = x ** 2
        foo = p(x, y)
        point.next = foo
        point = foo

    print(">>> %s" % c)

    bar = root
    ccc = 0
    while bar is not None:
        print(bar)
        bar = bar.get_next()
        ccc += 1
        if ccc > 20:
            import ipdb; ipdb.set_trace()
    #import ipdb; ipdb.set_trace()
    import sys; sys.exit(0)

    
    #import ipdb; ipdb.set_trace()
    config.quality = "low_quality"
    #config.aspect_ratio = 1
    config.frame_height = 15
    config.frame_width = 15
    scene = W()
    scene.render()
