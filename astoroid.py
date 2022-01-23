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
        for j, number in enumerate(point.point):
            try:
                next_ = seq[i + 1].point[j]
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
            line_start_point = [n.r for n in seq[i + 1].point]
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

    raise Exception("wat")
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
        r = kwargs.get("r")
        f = kwargs.get("f")
        m = kwargs.get("m")

        self.n = n
        self.modulus = modulus
        self.r = r if r is not None else self.n % self.modulus
        self.f = f if f is not None else self.n - self.r
        self.m = m if m is not None else self.f // self.modulus

    def __repr__(self):
        return "%.3f(r=%.3f,f=%.3f,m=%.3f)" % (self.n, self.r, self.f, self.m)


class ModularPoint:
    def __init__(self, point, modulus):
        self.point = [ModularNumber(n, modulus) for n in point]


if __name__ == "__main__":
    from manim import *
    scene = Scene()
    points = []
    m = 10
    modulus = 10
    for n in fdrange(0, 20, 0.089):
        points.append((n, n ** 2))
    modular_points = [ModularPoint(p, modulus) for p in points]
    lines = get_lines(modular_points, modulus)
    regular_porabola = VGroup(color=GREEN)
    regular_porabola.set_points_as_corners(
        [(float(p[0]), float(p[1]), 0) for p in points]
    )
    scene.add(regular_porabola)
    for line in lines:
        modular_porabola = VGroup(color=RED)
        myline = [(float(l[0]), float(l[1]), 0) for l in line]
        modular_porabola.set_points_as_corners(myline)
        scene.add(modular_porabola)
    scene.render()
