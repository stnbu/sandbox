# -*- Mode: Python

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

class Monty:
    def __init__ (self, N, R):
        self.N = N
        self.R = R
        self.R1 = modinv (R, N)
        self.N1 = (self.R1 * R) // N
        self.R2N = (R * R) % N
        #print("N = %s" % i2b(self.N))

    def redc (self, T):
        m = mod (mod (T, self.R) * self.N1, self.R)
        t = (T + m * self.N) // self.R
        if not t < self.N:
            return t - self.N
        else:
            return t

    def tm (self, a):
        return mod (a * self.R, self.N)

    def fm (self, a):
        return self.redc (a)

def full_monty(i, j):
    mP = Monty (1021, 1024)
    iP = mP.tm (i)
    jP = mP.tm (j)
    s = mP.fm (iP + jP)
    assert s == mod (i + j, 1021)
    d = mP.fm (iP - jP)
    assert d == mod (i - j, 1021)
    p = mP.fm (mP.redc (iP * jP))
    assert p == mod (i * j, 1021)

def i2b(i):
    return format(i, '#016b')

if __name__ == '__main__':
    full_monty(0, 0)
    full_monty(512, 512)
    full_monty(123, 321)
    full_monty(1023, 1023)
