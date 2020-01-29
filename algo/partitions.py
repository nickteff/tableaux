# %%
from bisect import bisect
import numpy as np
from sympy.combinatorics import Permutation

from algo import permutations


def partitions(n):
    p = [1 for i in range(n)]
    P = [p]

    N = 0
    while [n] not in P:
        p = P[N].copy()
        l = len(p)
        q = p[-1]

        if q > 1:
            p[-1] = q - 1
            q = 1
        else:
            p = p[:-1]

        for i in range(l - 1):
            pp = p.copy()
            if i == 0:
                pp[0] = min(pp[0] + 1, n)
                if pp in P:
                    continue
                else:
                    P.append(pp)
                    continue

            elif pp[i] < pp[i - 1]:
                pp[i] += 1
                if sum(pp) > n:
                    continue
                elif pp in P:
                    continue
                else:
                    P.append(pp)
                    continue
            else:
                continue
        N += 1

    P.sort()
    P.reverse()
    return P


def K(n):
    coefs = {}
    inner = {tuple(q): 0 for q in partitions(n)}
    for p in partitions(n):
        # print(p)
        coefs[tuple(p)] = inner.copy()
        seq = [[i + 1] * p[i] for i in range(len(p))]
        seq = [i for sub in seq for i in sub]
        q = []
        for perm in permutations(seq):
            if perm not in q:
                P, Q = RSK(perm)
                q.append(perm)
                if reading_word(Q) == list(range(1, n + 1)):
                    coefs[tuple(p)][shape(P)] += 1

    coefs = [coefs[p][i] for p in list(coefs) for i in list(coefs[p])]
    coefs = np.array(coefs).reshape(len(inner), len(inner)).T
    return coefs


def RSK(p):
    """Given a permutation p, spit out a pair of Young tableaux"""
    P = [];
    Q = []

    def insert(m, n=0):
        """Insert m into P, then place n in Q at the same place"""
        for r in range(len(P)):
            if m >= P[r][-1]:
                P[r].append(m);
                Q[r].append(n)
                return
            c = bisect(P[r], m)
            P[r][c], m = m, P[r][c]
        P.append([m])
        Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i + 1)
    return (P, Q)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def max_P(P):
    return max(max(P[r]) for r in range(len(P)))


def min_P(P):
    return min(min(P[r]) for r in range(len(P)))


def shape(P):
    return tuple(len(P[r]) for r in range(len(P)))


def content(P):
    j = 0
    t = []
    for i in range(max_P(P) + 1):
        t.append(0)
        for r in range(len(P)):
            for c in range(len(P[r])):
                if P[r][c] == i:
                    t[i] = t[i] + 1
    t.sort(reverse=True)
    # t = [i for i in t if i > 0]
    return tuple(t)


def h_gen(n):
    hh = [[i for i in range(1, n + 1)]]
    j = 0
    h = hh[0]
    while h != [n for i in range(n)]:
        for i in range(n - 1):
            if h[i] < h[i + 1]:
                h_new = h.copy()
                h_new[i] = h[i] + 1
                if h_new not in hh:
                    hh.append(h_new)
        j = j + 1
        h = hh[j]
    return hh


def incomparable(i, h):
    top = h[i - 1]
    bottom = min([j + 1 for j in range(len(h)) if h[j] >= i])
    return list(range(bottom, top + 1))


def h_function(i, n):
    return [min(j + i, n) for j in range(n)]


def PRSK(p, h=1):
    '''Given a permutation p, spit out a pair P a P_n,k tableaux and Q a standard Young tableaux
    -- See Sundquist, Wagner, West'''
    P = []
    Q = []
    if type(h) == int:
        h = h_function(h, len(p))
    p = p[::-1]

    def insert(m, n, h):
        '''Insert m into P, then place n in Q at the same place'''
        chk = incomparable(m, h)
        for r in range(len(P)):
            if len(intersection(chk, P[r])) == 2:
                continue
            elif len(intersection(chk, P[r])) == 1:
                o = intersection(chk, P[r])[0]
                c = P[r].index(o)
                P[r][c], m = m, P[r][c]
                chk = incomparable(m, h)
                continue
            elif m > P[r][-1]:
                P[r].append(m)
                Q[r].append(n)
                return
            else:
                c = bisect(P[r], m)
                P[r][c], m = m, P[r][c]
                chk = incomparable(m, h)

        P.append([m])
        Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i + 1, h)

    P = transpose(P)
    Q = transpose(Q)

    return (P, Q)


def transpose(P):
    """
    Returns the transpose of a tableau
    """
    PP = []
    for i in range(len(P)):
        for j in range(len(P[i])):
            PP.append([j, P[i][j]])

    n = max_P(P)
    ind = [[k[1] for k in PP if k[0] == j] for j in range(n + 1)]

    p = []
    for i in range(len(ind)):
        if len(ind[i]) != 0:
            p.append(ind[i])
    return p


def P_inv(P, h):
    inv = 0
    n = max(reading_word(P))
    columns = {
        i: P[r].index(i)
        for r in range(len(P))
        for i in range(1, n + 1)
        if i in P[r]
    }
    for i in range(1, n + 1):
        m = min(n, max(incomparable(i, h)))
        for j in range(i + 1, m + 1):
            if j > n:
                continue
            if columns[i] > columns[j]:
                inv += 1
    return inv


def coef(n, h):
    if type(h) == int:
        h = h_function(h, n)
    coefs = {i: {} for i in range(sum(range(n + 1)) + 1)}
    for p in permutations(range(1, n + 1)):
        P, Q = PRSK(p, h)
        if reading_word(Q) == list(range(1, n + 1)):
            if shape(P) in list(coefs[P_inv(P, h)].keys()):
                coefs[P_inv(P, h)][shape(P)] += 1
            else:
                coefs[P_inv(P, h)][shape(P)] = 1

    coefs = {i: coefs[i] for i in coefs.keys() if coefs[i] != {}}
    return coefs


def perm_coefs(n, h):
    k = np.linalg.inv(K(n))
    C = coef(n, h)
    pc = []
    for i in range(len(C.keys())):
        v = []
        for p in partitions(n):
            if tuple(p) in list(C[i].keys()):
                v.append(C[i][tuple(p)])
            else:
                v.append(0)
        pc.append(k @ np.array(v))
    return np.array(pc)


partitions(8)


def reading_word(P):
    return [item for sublist in P for item in sublist]
