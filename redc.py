# -*- Mode: Python

# GCD of 102 and 38
#
# divmod(102, 38) == (2, 26)
# divmod(38, 26) == (1, 12)
# divmod(26, 12) == (2, 2)
# divmod(12, 2) == (6, 0)
#
#
#
#
#
#
#
#
#

def egcd (a, b):
    if a == 0:
        return b, 0, 1
    else:
        q, r = divmod (b, a)
        g, y, x = egcd (r, a)
        return g, x - q * y, y

class NoInverse (Exception):
    pass

def modinv (a, p):
    if a < 0:
        return p - modinv (-a, p)
    else:
        g, x, y = egcd (a, p)
        if g != 1:
            raise NoInverse (a)
        else:
            return x % p

def mod (n, m):
    r = n % m
    if r < 0:
        return n - r
    else:
        return r

def i2b(i):
    return format(i, '#016b')

class Monty:
    def __init__ (self, N, R):
        self.N = N
        self.R = R
        self.R1 = modinv (R, N)
        self.N1 = (self.R1 * R) // N
        self.R2N = (R * R) % N
        print("N = %s" % i2b(self.N))

    def redc (self, T):
        m = mod (mod (T, self.R) * self.N1, self.R)
        t = (T + m * self.N) // self.R
        #assert mod (T + m * self.N, self.R) == 0
        if not t < self.N:
            return t - self.N
        else:
            return t

    def tm (self, a):
        return mod (a * self.R, self.N)

    def fm (self, a):
        return self.redc (a)

mP = Monty (1021, 1024)
mN = Monty (1009, 1021)

def fNP (n):
    return mN.fm (mP.fm (n))

def tNP (n):
    return mP.tm (mN.tm (n))

b = 700
c = 731

Pb = mP.tm (b)
Pc = mP.tm (c)

NPb = tNP (b)
NPc = tNP (c)

def t0():
    # do a complete test of operations with monty (1021, 1024)
    for i in range (1021):
        iP = mP.tm (i)
        for j in range (1021):
            jP = mP.tm (j)
            s = mP.fm (iP + jP)
            assert s == mod (i + j, 1021)
            d = mP.fm (iP - jP)
            assert d == mod (i - j, 1021)
            p = mP.fm (mP.redc (iP * jP))
            assert p == mod (i * j, 1021)

def t1():
    # test N->P monty.  first failure at 700,731.
    # it's always off by one or zero.
    for i in range (700, 800):
        for j in range (700, 800):
            x = (i + j) % 1009
            y = fNP (tNP (i) + tNP (j))
            if x != y:
                raise ValueError ((i,j))

if __name__ == '__main__':
    t1()
