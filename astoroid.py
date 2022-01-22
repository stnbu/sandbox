from decimal import Decimal

class p:
    modulus = Decimal(10)

    def __init__(self, x):
        self.next = None
        self.x = x if isinstance(x, Decimal) else Decimal(x)
        self.r = self.x % self.modulus
        self.f = self.x - self.r
        self.m = self.f // self.modulus

    def iter_lines(self):
        pass

    def get_next(self):
        return self.next

    def __repr__(self):
        return "<%.4f> (r=%.4f, f=%.4f, m=%.4f)" % (
            self.x,
            self.r,
            self.f,
            self.m
        )

point = p(0)
root = point
m = 10
for n in range(int(0*m), int(300*m), int(1.1*m)):
    foo = p(n/m)
    point.next = foo
    point = foo

ap = []
lines = []
bar = root
line = []

while bar is not None:
    ap.append(bar)
    next_ = bar.get_next()
    line.append(bar)
    if next_ is not None and next_.m != bar.m: # assumes positive monotonic
        end = p(bar.f + bar.modulus)
        end.m = bar.m
        end.f = bar.f
        line.append(end)
        lines.append(line)
        start = p(next_.f)
        line = [start]
    bar = next_

def eq(a, b):
    diff = abs(float(a) - float(b))
    return diff < 0.0001

x = ap[10]
assert eq(x.x, 9.9)
assert eq(x.r, 9.9)
assert eq(x.f, 0.0)
assert eq(x.m, 0.0)

x = ap[11]
assert eq(x.x, 11.0)
assert eq(x.r, 1.0)
assert eq(x.f, 10.0)
assert eq(x.m, 1.0)

x = ap[12]
assert eq(x.x, 12.1)
assert eq(x.r, 2.1)
assert eq(x.f, 10.0)
assert eq(x.m, 1.0)
