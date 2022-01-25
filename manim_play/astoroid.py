#!/usr/bin/env python3

from decimal import Decimal


def get_lines(modular_points):
    line = []
    lines = []
    for previous, current, next in zip([None] + modular_points, modular_points, modular_points[1:]):
        point = []
        wraps = False
        for i in range(0, len(current)):
            if current[i].m == next[i].m:
                point.append(current[i].r)
                continue
            wraps = True
            if next[i].m - current[i].m > 0 and next[i].r > current[i].r:
                point.append(modulus)
            elif next[i].m - current[i].m < 0 and next[i].r < current[i].r:
                point.append(-modulus)
            else:
                point.append(current[i].r)
        line.append(point)
        if wraps:
            lines.append(line)
            line = []
    #import ipdb; ipdb.set_trace()
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
    return np.array([float(xy_point[0]), float(xy_point[1]), 0])
    # try:
    #     return np.array([float(xy_point[0]), float(xy_point[1]), 0])
    # except:
    #     import ipdb; ipdb.set_trace()


if __name__ == "__main__":

    from manim import *

    config.frame_width = 20
    config.frame_height = 20

    scene = Scene()
    points = []
    modulus = Decimal(10)

    for i, n in enumerate(fdrange(0, 7, 0.01)):
        points.append((n, n ** 3))

    modular_points = [[ModularNumber(n, modulus) for n in point] for point in points]
    dotpacity = 0.5
    for line in get_lines(modular_points):
        #import ipdb; ipdb.set_trace()
        modular_porabola = VGroup(color=get_ith_color(i))
        modular_porabola.set_points_as_corners([to_xyz(l) for l in line])
        scene.add(modular_porabola)

    scene.render()
