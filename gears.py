#!/usr/bin/env python3


def rational_mul(a, b):
    a1, a2 = a
    b1, b2 = b
    return a1 * b1, a2 * b2


def rational_add(a, b):
    a1, a2 = a
    b1, b2 = b
    return a1 * b2 + b1 * a2, a2 * b2


class Gear:
    def __init__(self, ratio, parent=None):
        self.ratio = ratio
        self.angle = (0, 1)
        self.children = []
        self.is_root = parent is None
        if not self.is_root:
            parent.children.append(self)

    def turn(self, amount):
        my_amount = rational_mul(amount, self.ratio)
        new_angle = rational_add(self.angle, my_amount)
        self.angle = new_angle
        for child in self.children:
            child.turn(my_amount)


if __name__ == "__main__":

    g0 = Gear((1, 1))
    g1 = Gear((2, 1), g0)
    g2 = Gear((2, 1), g1)

    g0.turn((1, 1))
    print(g0.children[0].children[0].angle)

    wiggle = 0.0000000001

    def test_add(a, b):
        a1, a2 = a
        b1, b2 = b
        x, y = rational_add((a1, a2), (b1, b2))
        assert abs(x / y - (a1 / a2 + b1 / b2)) < wiggle

    def test_mul(a, b):
        a1, a2 = a
        b1, b2 = b
        x, y = rational_mul((a1, a2), (b1, b2))
        assert abs(x / y - ((a1 / a2) * (b1 / b2))) < wiggle

    test_add((1, 2), (3, 4))
    test_add((9, 3), (8, 5))
    test_add((25, 3), (4, 8))
    test_mul((1, 2), (3, 4))
    test_mul((9, 3), (8, 5))
    test_mul((25, 3), (4, 8))
