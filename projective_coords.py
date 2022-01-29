#!/usr/bin/env python3

from itertools import product

def get_slope(a, b, P):
    return (b[1] - b[0]) % P, (a[1] - b[0]) % P

def get_points(A, B, P):
    points = set()
    for x in range(0, P):
        for y in range(0, P):
            if (y**2) % P == (x**3 + A * x + B) % P:
                points.add((x % P, y % P))
    return points

def get_slopes(points, P):
    slopes = set()
    for a, b in product(points, points):
        if (a, b) in slopes or (b, a) in slopes:
            continue
        slopes.add(get_slope(a, b, P))
    return slopes

A = 2
B = 2
P = 17

points = get_points(A, B, P)
slopes = get_slopes(points, P)


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
    len_points = len(points),
    len_slopes = len(slopes),
    intersection = points & slopes,
    slopes=slopes,
    points=points
    
))
#""".format(*globals(), P=P, A=A, B=B))
