from decimal import Decimal


class ModularDecimal:
    def __init__(self, x, modulus):
        self.x = x if isinstance(x, Decimal) else Decimal(x)
        self.modulus = modulus
        self.next = None
        self.r = self.x % self.modulus  # `r`emainder
        self.f = self.x - self.r  # `f`loor
        self.mm = self.f // self.modulus  # `m`odulus `m`ultiple

    def iter_lines(self):
        line = []
        lines = []
        current = self
        while current is not None:
            next_ = current.get_next()
            line.append(current.r)
            if (
                next_ is not None and next_.mm != current.mm
            ):  # assumes positive monotonic
                end = self.__class__(current.f + current.modulus, self.modulus)
                end.mm = current.mm
                end.f = current.f
                line.append(end.r)
                lines.append(line)
                start = self.__class__(next_.f, self.modulus)
                line = [start.r]
            current = next_
        return lines  # we can/should generator this mofo

    def append(self, next_val):
        next_ = self.__class__(next_val, self.modulus)
        self.next = next_
        return self.next

    def get_next(self):
        return self.next

    def __repr__(self):
        return "<%.3f> (r=%.3f,f=%.3f,m=%.3f)" % (self.x, self.r, self.f, self.mm)


root = None
previous = None
m = 10
modulus = 10
for n in range(int(0 * m), int(300 * m), int(1.1 * m)):
    current = ModularDecimal(n / m, modulus)
    if previous is not None:
        previous.next = current
    previous = current
    if root is None:
        root = current

from manim import *
scene = Scene()
for i, line in enumerate(root.iter_lines()):
    vg = VGroup(color=RED)
    vg.set_points_as_corners([(float(x) + i, float(x), 0.0) for x in line])
    scene.add(vg)
scene.render()

ap = []
val = root
while True:
    ap.append(val)
    val = val.get_next()
    if val is None:
        break


def eq(a, b):
    diff = abs(float(a) - float(b))
    return diff < 0.0001


x = ap[9]
assert eq(x.x, 9.9)
assert eq(x.r, 9.9)
assert eq(x.f, 0.0)
assert eq(x.mm, 0.0)

x = ap[10]
assert eq(x.x, 11.0)
assert eq(x.r, 1.0)
assert eq(x.f, 10.0)
assert eq(x.mm, 1.0)

x = ap[11]
assert eq(x.x, 12.1)
assert eq(x.r, 2.1)
assert eq(x.f, 10.0)
assert eq(x.mm, 1.0)
