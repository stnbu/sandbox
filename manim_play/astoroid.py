#!/usr/bin/env python3

from decimal import Decimal

_POSITIVE = True
_NEGATIVE = False


def get_lines(modular_points, modulus):
    line = []
    lines = []
    for current, next in zip(modular_points, modular_points[1:]):
        new_point = []
        will_wrap = {}
        #import ipdb; ipdb.set_trace()
        for j, number in enumerate(current):
            if next[j].m > number.m:
                will_wrap[j] = _POSITIVE
            if next[j].m < number.m:
                will_wrap[j] = _NEGATIVE
            new_point.append(number.r)
        #import ipdb; ipdb.set_trace()
        line.append(new_point)
        if will_wrap:

            line_end_point = new_point[:]
            line_start_point = [n.r for n in next]
            for j, direction in will_wrap.items():
                if direction == _POSITIVE:
                    # Special surgery.
                    if new_point[j] == 0:
                        import ipdb; ipdb.set_trace()
                        line[-1][j] = modulus
                    line_end_point[j] = modulus
                    line_start_point[j] = 0
                if direction == _NEGATIVE:
                    line_end_point[j] = 0
                    line_start_point[j] = modulus
            line.append(line_end_point)
            lines.append(line)
            line = [line_start_point]
            will_wrap = {}
    
    return lines


def fdrange(x, y, step):
    x = Decimal(x)
    y = Decimal(y)
    step = Decimal(step)
    while x < y:
        yield x
        x += step


class ModularNumber:
    def __init__(self, n, modulus, **kwargs):
        # if abs(modulus + n) < 0.001:
        #     import ipdb; ipdb.set_trace()
        self.n = n
        self.modulus = modulus
        self.r = self.n % self.modulus
        self.f = self.n - self.r
        self.m = self.f // self.modulus

    def __repr__(self):
        return "%.3f(r=%.3f,f=%.3f,m=%.3f)" % (self.n, self.r, self.f, self.m)

def get_ith_color(i):
    colors = [
        "#e0ffff",
        "#00ffff",
        "#00ffff",
        "#7fffd4",
        "#66cdaa",
        "#afeeee",
        "#40e0d0",
        "#48d1cc",
        "#00ced1",
        "#20b2aa",
        "#5f9ea0",
        "#008b8b",
        "#008080",
    ]
    return colors[i % len(colors)]

def to_xyz(xy_point):
    return np.array([
        float(xy_point[0]),
        float(xy_point[1]),
        0
    ])

if __name__ == "__main__":

    from manim import *

    scene = Scene()
    points = []
    modulus = Decimal(10)

    for n in fdrange(-10.1, -9.9, 0.07):
        print(n)
        points.append((n, n**2))

    modular_points = [[ModularNumber(n, modulus) for n in point] for point in points]
    dotpacity = 0.5
    for i, line in enumerate(get_lines(modular_points, modulus)):
        modular_porabola = VGroup(color=get_ith_color(i))
        modular_porabola.set_points_as_corners(
            [to_xyz(l) for l in line]
        )
        scene.add(modular_porabola)
        for p in line:
            circle = Circle(radius=0.05, color=GREEN, fill_opacity=dotpacity, stroke_opacity=dotpacity)
            circle.move_to(np.array(to_xyz(p)))
            label = Text("%.2f,%.2f" % (p[0], p[1])).scale(0.15)
            label.next_to(circle, (UP+RIGHT)*0.5)
            scene.add(circle, label)

    regular_porabola = VGroup(color=GREEN)
    regular_porabola.set_points_as_corners(
        [(float(p[0]), float(p[1]), 0) for p in points]
    )
    scene.add(regular_porabola)

    scene.render()
