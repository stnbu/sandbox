#!/usr/bin/env python3

from decimal import Decimal
import numpy as np


def rgb_to_hex(*channels):
    return "#" + "".join([hex(c)[2:].zfill(2) for c in channels])


def gen_color_gradient(s, e, n):
    sr, sg, sb = s
    er, eg, eb = e
    for i in range(n):
        delta = float(i) / float(n)
        yield rgb_to_hex(
            sr + round(delta * (er - sr)),
            sg + round(delta * (eg - sg)),
            sb + round(delta * (eb - sb)),
        )


def to_manim_point(x, y, z=0):
    return np.array([float(x), float(y), float(z)])


def get_lines(modular_points, modulus):
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
