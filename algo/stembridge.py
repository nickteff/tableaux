import numpy as np
from sympy.combinatorics import Permutation
from .perms import permutations
from .partitions import RSK


def max_move(p):
    """
    Given a non-identity permutation caluculate the max
    1 <= i <= n so that p(i) != i
    """
    return max([i for i in range(len(p)) if i != p[i]])


def get_cycle(p):
    """
    Return the cycle the contains the max non-fixed point of p in the order required in Stembridge
    """
    m = max_move(p)
    for c in Permutation(p).full_cyclic_form:
        if m in c:
            l = len(c)
            z = c.index(m)
            return [c[(z + i) % l] for i in range(l)]


def get_r(p):
    """
    Get the r from Stembridge's algorithm
    """
    r = 0
    c = get_cycle(p)
    while r < len(c):
        if c[r] > c[(r + 1) % len(c)]:
            r += 1
        else:
            return r


def get_s(p):
    """
    Get the s from Stembridge's algorithm
    """
    c = get_cycle(p)
    r = get_r(p)
    ss = []
    for s in range(r, len(c)):
        if c[s] > c[(s + 1) % len(c)]:
            ss.append(s)
        if c[r - 1] <= c[(s + 1) % len(c)]:
            ss.append(s)
    return min(ss)


def new_perm(p):
    """
    Given a non-trivial permutation what is the next reduced
    permutations from Stembridge's algorithm
    """
    pp = Permutation(p).full_cyclic_form
    m = max_move(p)
    c = get_cycle(p)
    l = len(c)
    s = get_s(p)
    cm = [i for i in range(len(pp)) if m in pp[i]][0]
    if s == l - 1:
        del pp[cm]
        return Permutation(pp).array_form
    else:
        del c[1:s + 1]
        pp[cm] = c
        return Permutation(pp).array_form


def new_triple(p, a, f):
    """
    Given a triple p a permutation, a a sequence, and f an index function.  Return the next triple from Stembridge's algorithm
    """
    k = max(a)
    pp = Permutation(p).full_cyclic_form
    m = max_move(p)
    c = get_cycle(p)
    l = len(c)
    r = get_r(p)
    s = get_s(p)
    cm = [i for i in range(len(pp)) if m in pp[i]][0]
    if s == l - 1:
        del pp[cm]
        p = Permutation(pp).array_form
        for i in c:
            a[i] = k + 1
        f[k + 1] = l - r
    else:
        for i in c[1:s + 1]:
            a[i] = k + 1
        if c[s] > c[(s + 1) % l]:
            f[k + 1] = s - r
        if c[r - 1] <= c[(s + 1) % l]:
            f[k + 1] = s - r + 1
        del c[1:s + 1]
        pp[cm] = c
        p = Permutation(pp).array_form
    return p, a, f


def code(p):
    """
    Calculate the marked code of a permutation
    -- See Stembridge
    """
    a = np.zeros_like(p)
    f = {0: 0}
    while p != list(range(len(p))):
        p, a, f = new_triple(p, a, f)
    return list(a), f


def all_perms(n):
    """
    Iteration over all of the permutations of [n]
    """
    for p in permutations(range(n)):
        a, f = code(p)
        p = [1 + i for i in p]
        print(p, RSK(a), f)
