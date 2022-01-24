from decimal import Decimal

START = 0
END = 1


def get_lines(modular_points, modulus):
    seq = list(modular_points)
    line = []
    lines = []
    for i, point in enumerate(seq):
        new_point = []
        will_wrap = {}
        for j, number in enumerate(point):
            try:
                next_ = seq[i + 1][j]
            except IndexError:
                return lines
            if next_.m != number.m:
                if next_.m > number.m:
                    will_wrap[j] = 1
                else:
                    will_wrap[j] = -1
            new_point.append(number.r)
        line.append(new_point)
        if will_wrap:
            line_end_point = new_point[:]
            line_start_point = [n.r for n in seq[i + 1]]
            for j, direction in will_wrap.items():
                if direction == 1:
                    line_end_point[j] = modulus
                    line_start_point[j] = 0
                if direction == -1:
                    line_end_point[j] = 0
                    line_start_point[j] = modulus
            line.append(line_end_point)
            lines.append(line)
            line = [line_start_point]
            will_wrap = {}


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


if __name__ == "__main__":
    from manim import *

    scene = Scene()
    points = []
    m = 10
    modulus = 10

    for n in fdrange(0, 20, 0.01):
        points.append((n, n ** 2))

    modular_points = [[ModularNumber(n, modulus) for n in point] for point in points]
    for line in get_lines(modular_points, modulus):
        modular_porabola = VGroup(color=RED)
        modular_porabola.set_points_as_corners(
            [(float(l[0]), float(l[1]), 0) for l in line]
        )
        scene.add(modular_porabola)

    regular_porabola = VGroup(color=GREEN)
    regular_porabola.set_points_as_corners(
        [(float(p[0]), float(p[1]), 0) for p in points]
    )
    scene.add(regular_porabola)

    scene.render()
