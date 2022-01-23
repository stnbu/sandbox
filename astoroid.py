from decimal import Decimal
from collections import namedtuple
from manim import *

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

START = 0
END = 1

# def iter_lines(seq):
#     line = []
#     lines = []
#     current = self
#     seq = list(seq)

def get_lines(modular_points, modulus):
    seq = list(modular_points)
    line = []
    lines = []
    for i, point in enumerate(seq):
        new_point = []
        fake_points = None
        for j, number in enumerate(point.point):
            #import ipdb; ipdb.set_trace()
            try:
                next_ = seq[i+1].point[j]
            except IndexError:
                #line.append(new_point)
                #import ipdb; ipdb.set_trace()
                break
            ######
            ######
            if next_.m != number.m:
                if fake_points is None:
                    fake_points = [
                        [None] * len(point.point),
                        [None] * len(point.point)
                    ] # FIXME
                # FIXME -- "detect" direcation, act approprately
                fake_points[START][j] = 0
                fake_points[END][j] = modulus
                #import ipdb; ipdb.set_trace()
            ######
            ######
            new_point.append(number.r)
        else:
            line.append(new_point)
        if fake_points is not None:
            
            for j in range(0, len(point.point)):
                if fake_points[START][j] is None:
                    fake_points[START][j] = seq[i+1].point[j].n
                if fake_points[END][j] is None:
                    fake_points[END][j] = seq[i].point[j].n
                #import ipdb; ipdb.set_trace()
            #import ipdb; ipdb.set_trace()
            line.append(fake_points[END])
            lines.append(line)
            line = [fake_points[START]]
            fake_points = None
    else:
        #import ipdb; ipdb.set_trace()
        lines.append(line)
    #import ipdb; ipdb.set_trace()
    return lines

#     for i, current in enumerate(seq):
#         next_ = seq[i+1]
#         line.append(current.r)
#         if next_.mm != current.mm:
#             end = current.f + current.modulus, self.modulus
#             end.mm = current.mm
#             end.f = current.f
#             line.append(end.r)
#             lines.append(line)
#             start = self.__class__(next_.f, self.modulus)
#             line = [start.r]
#         current = next_
#     return lines  # we can/should generator this mofo


regular_porabola = VGroup(color=GREEN)
modular_porabola = VGroup(color=RED)

#    vg.set_points_as_corners([(float(x) + i, float(x), 0.0) for x in line])
#    scene.add(vg)


def fdrange(x, y, step):
    x = Decimal(x)
    y = Decimal(y)
    step = Decimal(step)
    while x < y:
        yield x
        x += step


scene = Scene()

points = []
        
m = 10
modulus = 10
for n in fdrange(0, 20, 0.089):
    points.append((n, n**2))


modular_points = [ModularPoint(p, modulus) for p in points]
#import ipdb; ipdb.set_trace()
fooo = get_lines(modular_points, modulus)
#import ipdb; ipdb.set_trace()
import sys; sys.exit(0)
#modular_points = list(iter_modular_points(points, modulus))

regular_porabola.set_points_as_corners([(float(p[0]), float(p[1]), 0) for p in points])
modular_porabola.set_points_as_corners([(float(p[0]), float(p[1]), 0) for p in fooo])

scene.add(regular_porabola)

scene.render()

# from manim import *
# scene = Scene()
# for i, line in enumerate(root.iter_lines()):
#     vg = VGroup(color=RED)
#     vg.set_points_as_corners([(float(x) + i, float(x), 0.0) for x in line])
#     scene.add(vg)
# scene.render()


# class ModularDecimal:
#     def __init__(self, x, modulus):
#         self.x = x if isinstance(x, Decimal) else Decimal(x)
#         self.modulus = modulus
#         self.next = None
#         self.r = self.x % self.modulus  # `r`emainder
#         self.f = self.x - self.r  # `f`loor
#         self.mm = self.f // self.modulus  # `m`odulus `m`ultiple

#     def iter_lines(self):
#         line = []
#         lines = []
#         current = self
#         while current is not None:
#             next_ = current.get_next()
#             line.append(current.r)
#             if (
#                 next_ is not None and next_.mm != current.mm
#             ):  # assumes positive monotonic
#                 end = self.__class__(current.f + current.modulus, self.modulus)
#                 end.mm = current.mm
#                 end.f = current.f
#                 line.append(end.r)
#                 lines.append(line)
#                 start = self.__class__(next_.f, self.modulus)
#                 line = [start.r]
#             current = next_
#         return lines  # we can/should generator this mofo

#     def append(self, next_val):
#         next_ = self.__class__(next_val, self.modulus)
#         self.next = next_
#         return self.next

#     def get_next(self):
#         return self.next

#     def __repr__(self):
#         return "<%.3f> (r=%.3f,f=%.3f,m=%.3f)" % (self.x, self.r, self.f, self.mm)

# def parabola(iter):
#     modulus = 10
#     pairs = []
#     for x, y in iter:
#         xx = ModularDecimal(x, modulus)
#         yy = ModularDecimal(y, modulus)
#         previous = None
#         pair = []
#         for t in [x, y]:
#             current = 
#             if previous is not None:
#                 previous.next = current
#             previous = current
#             if root is None:
#                 root = current
#             pair.append(current)
#         pairs.append(pair)

        
    
# root = None
# previous = None
# m = 10
# modulus = 10
# for n in range(int(0 * m), int(300 * m), int(1.1 * m)):
#     current = ModularDecimal(n / m, modulus)
#     if previous is not None:
#         previous.next = current
#     previous = current
#     if root is None:
#         root = current

# from manim import *
# scene = Scene()
# for i, line in enumerate(root.iter_lines()):
#     vg = VGroup(color=RED)
#     vg.set_points_as_corners([(float(x) + i, float(x), 0.0) for x in line])
#     scene.add(vg)
# scene.render()

# ap = []
# val = root
# while True:
#     ap.append(val)
#     val = val.get_next()
#     if val is None:
#         break


# def eq(a, b):
#     diff = abs(float(a) - float(b))
#     return diff < 0.0001


# x = ap[9]
# assert eq(x.x, 9.9)
# assert eq(x.r, 9.9)
# assert eq(x.f, 0.0)
# assert eq(x.mm, 0.0)

# x = ap[10]
# assert eq(x.x, 11.0)
# assert eq(x.r, 1.0)
# assert eq(x.f, 10.0)
# assert eq(x.mm, 1.0)

# x = ap[11]
# assert eq(x.x, 12.1)
# assert eq(x.r, 2.1)
# assert eq(x.f, 10.0)
# assert eq(x.mm, 1.0)
