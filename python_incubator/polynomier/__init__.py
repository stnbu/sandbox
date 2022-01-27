
from itertools import product

def combine(a, b):
    return a[0] + b[0], a[1] * b[1]

class Polynomial:
    def __init__(self, *coefficients, as_dict=None):
        if as_dict is None:
            self.coefficients = dict(enumerate(coefficients))
        else:
            self.coefficients = as_dict

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        new_coefficients = {i:-1 * c for (i,c) in other.coefficients.items()}
        return self + Polynomial(as_dict=new_coefficients)

    def __div__(self, other):
        remainder = None
        result = self
        while True:
            import ipdb; ipdb.set_trace()
            result -= other

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        indicies = set(
            list(self.coefficients.keys()) +
            list(other.coefficients.keys())
        )
        new_coefficients = {}
        for index in indicies:
            self_c = self.coefficients.get(index, 0)
            other_c = other.coefficients.get(index, 0)
            new_coefficients[index] = self_c + other_c
        return Polynomial(as_dict=new_coefficients)
    
    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            return Polynomial(as_dict={i:other*c for (i, c) in self.coefficients.items()})
        else:
            expanded = [combine(a, b)
                        for (a, b) in product(
                                self.coefficients.items(),
                                other.coefficients.items())
                        ]
            max_index = max(i for (i, c) in expanded)
            new_coefficients = {}
            for index in range(0, max_index + 1):
                new_coefficients[index] = sum([c for (i, c) in expanded if i == index])
            return Polynomial(as_dict=new_coefficients)

    def eval(self, x):
        return sum([c * x**i for i, c in self.coefficients.items()])

    @property
    def degree(self):
        return max(self.coefficients)

    def _get_term_repr(self, i):
        "how to implement shitty human syntax"
        c = self.coefficients.get(i, 0)
        if c == 0:
            return ""
        exponent = "" if i < 2 else "^%s" % i
        coefficient = "" if i > 0 and c == 1 else str(c)
        variable = "" if i < 1 else "x"
        oper = "" if i == self.degree else " + "
        if c < 0:
            oper = "-" if i == self.degree else " - "
            if len(coefficient) > 0:
                coefficient = coefficient.lstrip("-")
        return oper + coefficient + variable + exponent

    def __repr__(self):
        result = []
        for i in sorted(self.coefficients, reverse=True):
            result.append(self._get_term_repr(i))
        return "".join(result).lstrip(" +")

    
if __name__ == "__main__":
    p1 = Polynomial(0, 0, 1)
    print("p1 = %s" % p1)
    p2 = Polynomial(1, 0, 2)
    print("p2 = %s" % p2)
    p3 = p1 * p2
    print("p3 = p1 * p2 = %s" % p3)
    p4 = p3 + p2
    print("p4 = p3 + p2 = %s" % p4)
    p5 = p4 + 8
    print("p5 = p4 + 8 = %s" % p5)
    p6 = p3 - 8
    print("p6 = p3 - 8 = %s" % p6)
    p7 = p4 - p3
    print("p7 = p4 - p3 = %s" % p7)

    assert 36 == p3.eval(2)
    assert 4 == p1.eval(2)
    assert 9 == p2.eval(2)

    p8 = Polynomial(1, 1)
    p9 = Polynomial(1, 1)
    print("(%s) * (%s) = %s" % (p8, p9, p8 * p9))

    p10 = Polynomial(1, 1)
    p11 = Polynomial(-1, 1)
    print("(%s) * (%s) = %s" % (p10, p11, p10 * p11))


    p10 / p10