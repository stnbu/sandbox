from decimal import Decimal
from manim import *

START = 0
END = 1

def get_lines(modular_points, modulus):
    seq = list(modular_points)
    line = []
    lines = []
    for i, point in enumerate(seq):
        new_point = []
        fake_points = None
        for j, number in enumerate(point.point):
            try:
                next_ = seq[i+1].point[j]
            except IndexError:
                break
            if next_.m != number.m:
                if fake_points is None:
                    fake_points = [
                        [None] * len(point.point),
                        [None] * len(point.point)
                    ] # FIXME
                # FIXME -- "detect" direcation, act approprately
                fake_points[START][j] = 0
                fake_points[END][j] = modulus
            new_point.append(number.r)
        else:
            line.append(new_point)
        if fake_points is not None:
            
            for j in range(0, len(point.point)):
                if fake_points[START][j] is None:
                    fake_points[START][j] = seq[i+1].point[j].n
                if fake_points[END][j] is None:
                    fake_points[END][j] = seq[i].point[j].n
            line.append(fake_points[END])
            lines.append(line)
            line = [fake_points[START]]
            fake_points = None
    else:
        lines.append(line)
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
    scene = Scene()
    points = []
    m = 10
    modulus = 10
    for n in fdrange(0, 20, 0.089):
        points.append((n, n**2))
    modular_points = [ModularPoint(p, modulus) for p in points]
    fooo = get_lines(modular_points, modulus)
    regular_porabola = VGroup(color=GREEN)
    regular_porabola.set_points_as_corners([(float(p[0]), float(p[1]), 0) for p in points])
    scene.add(regular_porabola)
    for line in fooo[0:12]: # first wrapping of x happens with [0:12]
        modular_porabola = VGroup(color=RED)
        myline = [(float(l[0]), float(l[1]), 0) for l in line]
        modular_porabola.set_points_as_corners(myline)
        scene.add(modular_porabola)
    scene.render()
