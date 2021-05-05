#!/usr/bin/env python3

# notes, follow-along, theft from http://www.shirpeled.com/2018/09/a-hands-on-tutorial-for-zero-knowledge.html

import random

def get_witness(problem, assignment):
    """
    Given an instance of a partition problem via a list of numbers (the problem) and a list of
    (-1, 1), we say that the assignment satisfies the problem if their dot product is 0.
    """
    #breakpoint()
    sum = 0
    mx = 0    
    side_obfuscator = 1 - 2 * random.randint(0, 1)
    witness = [sum]
    assert len(problem) == len(assignment)
    for num, side in zip(problem, assignment):
        assert side == 1 or side == -1
        sum += side * num * side_obfuscator
        witness += [sum]
        mx = max(mx, num)
    # make sure that it is a satisfying assignment
    assert sum == 0
    shift = random.randint(0, mx)
    witness = [x + shift for x in witness]
    breakpoint()
    return witness

def partsums(l, m):
    assert len(l) == len(m)
    result = []
    for i in range(len(l)+1):
        result.append(dot(l[:i], m[:i]))
    return result

def dot(l, m):
    assert len(l) == len(m)
    result = 0
    for a, b in zip(l, m):
        result += a * b
    return result

def verify_for_i(l, m, i):
    breakpoint()
    assert len(l) == len(m)
    assert i >= 0
    assert i < len(l)
    p = partsums(l, m)
    if p == len(p) - 1:
        assert p[0] == 0 and p[-1] == 0
    else:
        assert abs(l[i] == abs(p[i + 1] - p[i]))

def foo():
    l = [4, 11, 8,  1]
    m = [1, -1, 1, -1]
    w = get_witness(l, m)
    #verify_for_i(l, m, 2)
    #d = dot(l, m)
    #p = partsums(l, m)
    print(p)

if __name__ == '__main__':
    foo()
