#!/usr/bin/env python3

from decimal import Decimal

def get_lines(modular_points):
    # FIXME: we need to adjust/fit the _start_ of lines too.
    modulus = Decimal(11)
    line = []
    lines = []
    was_modulated = []
    for current, next in zip(modular_points, modular_points[1:]):
        point = []
        wraps = False
        for i in was_modulated:
            current[i].r = 0
        was_modulated = []
        for i in range(0, len(current)):
            if current[i].m == next[i].m:
                point.append(current[i].r)
                continue
            wraps = True
            was_modulated.append(i)
            if next[i].m - current[i].m > 0 and next[i].r > current[i].r:
                point.append(modulus)
            elif next[i].m - current[i].m < 0 and next[i].r < current[i].r:
                point.append(-modulus)
            # elif next[i].m - current[i].m > 0 and next[i].r < current[i].r:
            #     point.append(0)
            # elif next[i].m - current[i].m < 0 and next[i].r > current[i].r:
            #     point.append(0)
            else:
                point.append(current[i].r)
        line.append(point)
        if wraps:
            lines.append(line)
            line = []
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

def _channel_to_hex(color_val: int) -> str:
    raw: str = hex(color_val)[2:]
    return raw.zfill(2)

def rgb_to_hex(red: int, green: int, blue: int) -> str:
    return "#" + _channel_to_hex(red) + _channel_to_hex(green) + _channel_to_hex(blue)


def adams_spectrum(i):
    red = 255
    green = 0
    blue = 0
    delta = 900 / i
    phase = 0
    colors = []
    while phase < 5:
        colors.append(rgb_to_hex(int(red) % 255, int(green) % 255, int(blue) % 255))
        if phase == 0 and green < 255:
            green += delta
            if green >= 255:
                phase = 1
        if phase == 1 and red > 60:
            red -= delta *2
            if red <= 60:
                phase = 2
        if phase == 2 and blue < 210:
            blue += delta
            if blue >= 210:
                phase = 3
        if phase == 3 and green > 60:
            green -= delta
            if green <= 60:
                phase = 4
        if phase == 4 and red < 210:
            red += delta
            if red >= 210:
                phase = 5
    return colors

def gen_color_gradient(s, e, n):
    sr, sg, sb = s
    er, eg, eb = e
    thing = []
    for i in range (n):
        delta = float(i)/float(n)
        thing.append(rgb_to_hex(
            sr + round(delta * (er - sr)),
            sg + round(delta * (eg - sg)),
            sb + round(delta * (eb - sb)),
        ))
    return thing

import numpy as np

def to_xyz(xy_point):
    return np.array([float(xy_point[0]), float(xy_point[1]), 0])
    # try:
    #     return np.array([float(xy_point[0]), float(xy_point[1]), 0])
    # except:
    #     import ipdb; ipdb.set_trace()


if __name__ == "__main__":
    colors = adams_spectrum(5)
    print(colors)
    print(len(colors))
    import sys; sys.exit(0)
    from manim import *

    config.frame_width = 20
    config.frame_height = 20

    scene = Scene()
    points = []
    modulus = Decimal(10)

    for i, n in enumerate(fdrange(-1000, 1000, 0.1)):
        points.append((n, n ** 3))

    modular_points = [[ModularNumber(Decimal(n), Decimal(modulus)) for n in point] for point in points]
    dotpacity = 0.5
    for line in get_lines(modular_points):
        #import ipdb; ipdb.set_trace()
        modular_porabola = VGroup(color=get_ith_color(i))
        modular_porabola.set_points_as_corners([to_xyz(l) for l in line])
        scene.add(modular_porabola)

    scene.render()
