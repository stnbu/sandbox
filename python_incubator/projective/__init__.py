#!/usr/bin/env python3

class pfloat(float):
    def __new__(cls, n):
        return super(pfloat, cls).__new__(cls, n)

    def infiniwrap(self, func, _, other):
        if other == float('inf') or other == float('-inf'):
            raise ValueError("Actual infinities unsupported.")
        result = func(self, other)
        if result == float('inf'):
            return self.__class__(-fmax)
        elif result == float('-inf'):
            return self.__class__(fmax)
        else:
            return self.__class__(other)

    def __add__(self, other):
        return self.infiniwrap(float.__add__, self, other)

if __name__ == "__main__":
    import sys
    fmax = sys.float_info.max

    big = pfloat(fmax)
    pig = pfloat(fmax)
    assert big + pig == -fmax