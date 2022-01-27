
from itertools import product

def combine(a, b):
    return a[0] + b[0], a[1] * b[1]

class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = dict(enumerate(coefficients))

    
    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            new_coefficients = {}
            for i, coefficient in self.coefficients.items:
                new_coefficients.append(other * coefficient)
            return Polynomial(*new_coefficients)
        else:
            degree_diff = abs(len(self.coefficients) - len(other.coefficients))
            padded_self = Polynomial(*(self.coefficients + [0] * (len(self.coefficients) - degree_diff)))
            padded_other = Polynomial(*(other.coefficients + [0] * (len(other.coefficients) - degree_diff)))
            expanded = [combine(a, b) for (a, b) in product(
                enumerate(padded_self.coefficients),
                enumerate(padded_other.coefficients)
            )]
            max_index = max(i for (i, c) in expanded)
            new_coefficients = []
            for index in range(0, max_index + 1):
                new_coeff = sum([c for (i, c) in expanded if i == index])
                new_coefficients.append(new_coeff)
            return Polynomial(*new_coefficients)

    def eval(self, x):
        return sum([c * x**i for i, c in self.coefficients.items()])

    @property
    def degree(self):
        return max(self.coefficients)

    def __repr__(self):
        def get_term(i, c):
            "how to implement shitty human syntax"
            exponent = "" if i < 2 else "^%s" % i
            coefficient = "" if i > 0 and c == 1 else str(c)
            variable = "" if i < 1 else "x"
            oper = " + "
            if c < 0:
                oper = "-" if i == self.degree else " - "
            return oper + coefficient + variable + exponent
        return "".join(
            reversed([get_term(i, c) for (i, c) in enumerate(self.coefficients) if c != 0])
        ).lstrip(" +")

    
if __name__ == "__main__":
    p1 = Polynomial(0, 0, 1)
    print("p1 = %s" % p1)
    p2 = Polynomial(1, 0, 2)
    print("p2 = %s" % p2)
    p3 = p1 * p2
    print("p1 * p2 = %s" % p3)
    assert 4 == p1.eval(2)
    assert 9 == p2.eval(2)
    assert 36 == p3.eval(2)
