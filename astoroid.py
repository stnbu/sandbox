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
bar = root
ccc = 0
while bar is not None:
    ap.append(bar)
    bar = bar.get_next()
    print('.', end='')
print('')

def eq(a, b):
    diff = abs(float(a) - float(b))
    if diff > 0.0001:
        raise AssertionError


"""
In [279]: ap[10]
Out[279]: <9.900> (r=9.900, f=0.000, m=0.000)

In [280]: ap[11]
Out[280]: <11.000> (r=1.000, f=10.000, m=1.000)

In [281]: ap[12]
Out[281]: <12.100> (r=2.100, f=10.000, m=1.000)
"""

x = ap[10]
eq(x.x, 9.9)
eq(x.r, 9.9)
eq(x.f, 0.0)
eq(x.m, 0.0)

x = ap[11]
eq(x.x, 11.0)
eq(x.r, 1.0)
eq(x.f, 10.0)
eq(x.m, 1.0)

x = ap[12]
eq(x.x, 12.1)
eq(x.r, 2.1)
eq(x.f, 10.0)
eq(x.m, 1.0)

