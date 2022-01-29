#!/usr/bin/env python3

from itertools import product


def get_gcd(x: int, y: int):
    if y == 0:
        return x
    return get_gcd(y, x % y)


def get_slope(a, b, P):
    return (b[1] - b[0]) % P, (a[1] - b[0]) % P


def get_points(A, B, P):
    points = set()
    for x in range(0, P):
        for y in range(0, P):
            if (y ** 2) % P == (x ** 3 + A * x + B) % P:
                points.add((x % P, y % P))
    return points


def get_slopes(points, P):
    slopes = set()
    for x, y in product(points, points):
        a, b = get_slope(x, y, P)
        gcd = get_gcd(a, b)
        a = int(a / gcd)
        b = int(b / gcd)
        if (a, b) not in slopes and (b, a) not in slopes:
            slopes.add((a, b))
    return slopes


A = 2
B = 2
P = 17

points = get_points(A, B, P)
slopes = get_slopes(points, P)

intersection = set()
for slope in slopes:
    if slope in points:
        intersection.add(slope)
    rslope = tuple(reversed(list(slope)))
    if rslope in points:
        intersection.add(rslope)

print(
    """
EC: y**2 % {P} == (x**3 + {A}*x + {B}) % {P}
len(points) == {len_points}
len(slopes) == {len_slopes}
slopes & points == {intersection}
-----
points = {points}
slopes = {slopes}
""".format(
        A=A,
        B=B,
        P=P,
        len_points=len(points),
        len_slopes=len(slopes),
        intersection=intersection,
        slopes=slopes,
        points=points,
    )
)
