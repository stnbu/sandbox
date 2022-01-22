from decimal import Decimal

class ModularNumberLine:
    modulus = Decimal(10)

    def __init__(self, x):
        self.next = None
        self.x = x if isinstance(x, Decimal) else Decimal(x)
        self.r = self.x % self.modulus    # `r`emainder
        self.f = self.x - self.r          # `f`loor
        self.mm = self.f // self.modulus  # `m`odulus `m`ultiple

    def iter_lines(self):
        line = []
        lines = []
        current = self
        while current is not None:
            next_ = current.get_next()
            line.append(current)
            if next_ is not None and next_.mm != current.mm: # assumes positive monotonic
                end = ModularNumberLine(current.f + current.modulus)
                end.mm = current.mm
                end.f = current.f
                line.append(end)
                lines.append(line)
                start = ModularNumberLine(next_.f)
                line = [start]
            current = next_
        return lines # we can/should generator this mofo

    def get_next(self):
        return self.next

    def __repr__(self):
        return "<%.3f> (r=%.3f,f=%.3f,m=%.3f)" % (
            self.x,
            self.r,
            self.f,
            self.mm
        )

point = ModularNumberLine(0)
root = point
m = 10
for n in range(int(0*m), int(300*m), int(1.1*m)):
    foo = ModularNumberLine(n/m)
    point.next = foo
    point = foo

more_lines = root.iter_lines()
    
ap = []
lines = []
bar = root
line = []

while bar is not None:
    ap.append(bar)
    next_ = bar.get_next()
    line.append(bar)
    if next_ is not None and next_.mm != bar.mm: # assumes positive monotonic
        end = ModularNumberLine(bar.f + bar.modulus)
        end.mm = bar.mm
        end.f = bar.f
        line.append(end)
        lines.append(line)
        start = ModularNumberLine(next_.f)
        line = [start]
    bar = next_

def eq(a, b):
    diff = abs(float(a) - float(b))
    return diff < 0.0001

x = ap[10]
assert eq(x.x, 9.9)
assert eq(x.r, 9.9)
assert eq(x.f, 0.0)
assert eq(x.mm, 0.0)

x = ap[11]
assert eq(x.x, 11.0)
assert eq(x.r, 1.0)
assert eq(x.f, 10.0)
assert eq(x.mm, 1.0)

x = ap[12]
assert eq(x.x, 12.1)
assert eq(x.r, 2.1)
assert eq(x.f, 10.0)
assert eq(x.mm, 1.0)
