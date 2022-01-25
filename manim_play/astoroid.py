#!/usr/bin/env python3

from decimal import Decimal

POSITIVE = True
NEGATIVE = False


def get_lines(modular_points, modulus):
    line = []
    lines = []
    for current, next in zip(modular_points, modular_points[1:]):
        new_point = []
        will_wrap = {}
        for j, number in enumerate(current):
            if number.n % modulus > 0.001:
                if next[j].m > number.m:
                    will_wrap[j] = POSITIVE
                if next[j].m < number.m:
                    will_wrap[j] = NEGATIVE
            new_point.append(number.r)
        #import ipdb; ipdb.set_trace()
        line.append(new_point)
        if will_wrap:
            
            line_end_point = new_point[:]
            line_start_point = [n.r for n in next]
            for j, direction in will_wrap.items():
                if direction == POSITIVE:
                    line_end_point[j] = modulus
                    line_start_point[j] = 0
                if direction == NEGATIVE:
                    line_end_point[j] = 0
                    line_start_point[j] = modulus
            line.append(line_end_point)
            if abs(line[0][1] - line[-1][1]) < 0.01:
                pass # import ipdb; ipdb.set_trace()
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


if __name__ == "__main__":
    from manim import *

    #config.frame_height = 20
    #config.frame_width = 20
    scene = Scene()
    points = []
    m = 10
    modulus = Decimal(10)



    for n in fdrange(-19.8, 19.8, 0.01):
        if abs(n % modulus) < 0.01:
            continue
        points.append((n, n ** 2))

    #line = VGroup(color=WHITE, stroke_width=1.5)
    #line.set_points_as_corners([[-20, 1, 0], [20, 1, 0]])
    #line.to_edge(DOWN)
    #scene.add(line)
    modular_points = [[ModularNumber(n, modulus) for n in point] for point in points]
    for line in get_lines(modular_points, modulus):
        modular_porabola = VGroup(color=PURPLE)
        modular_porabola.set_points_as_corners(
            [(float(l[0]), float(l[1]), 0) for l in line]
        )
        #modular_porabola.to_edge(DOWN)
        scene.add(modular_porabola)

    regular_porabola = VGroup(color=GREEN)
    regular_porabola.set_points_as_corners(
        [(float(p[0]), float(p[1]), 0) for p in points]
    )
    scene.add(regular_porabola)

    scene.render()
