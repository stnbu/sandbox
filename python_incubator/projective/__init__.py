#!/usr/bin/env python3


class pfloat(float):
    def __new__(cls, n):
        return super(pfloat, cls).__new__(cls, n)

    def infiniwrap(self, func, other):
        if other == float("inf") or other == float("-inf"):
            raise ValueError("Actual infinities unsupported.")
        result = func(self, other)
        if result == float("inf"):
            return self.__class__(-fmax)
        elif result == float("-inf"):
            return self.__class__(fmax)
        else:
            return self.__class__(result)

    def __add__(self, other):
        return self.infiniwrap(float.__add__, other)

    def __ceil__(self, other):
        return self.infiniwrap(float.__ceil__, other)

    def __mul__(self, other):
        return self.infiniwrap(float.__mul__, other)

    def __pow__(self, other):
        return self.infiniwrap(float.__pow__, other)

    def __radd__(self, other):
        return self.infiniwrap(float.__radd__, other)

    def __rmul__(self, other):
        return self.infiniwrap(float.__rmul__, other)

    def __rpow__(self, other):
        return self.infiniwrap(float.__rpow__, other)

    def __rsub__(self, other):
        return self.infiniwrap(float.__rsub__, other)

    def __rtruediv__(self, other):
        return self.infiniwrap(float.__rtruediv__, other)

    def __sub__(self, other):
        return self.infiniwrap(float.__sub__, other)

    def __truediv__(self, other):
        return self.infiniwrap(float.__truediv__, other)

    def __trunc__(self, other):
        return self.infiniwrap(float.__trunc__, other)


if __name__ == "__main__":
    import sys

    fmax = sys.float_info.max

    big = pfloat(fmax)
    pig = pfloat(fmax)
    assert big + pig == -fmax
    assert big * pig == -fmax

    assert big - pig == 0
    assert pig - big == 0
    assert -big - pig == fmax
    assert -big * pig == fmax

    # TODO: other-ops