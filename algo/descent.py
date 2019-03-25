from bisect import bisect_right
import numpy as np
from sympy.combinatorics import Permutation
from algo import descents, RSK
from algo import RSK

def max_descent(p):
    return max([p[i] for i in descents(p)])

def index_max_descent(p):
    return p.index(max_descent(p))


def find_valleys(p):
    return [i for i in range(1,len(p)-1) if p[i-1] > p[i] < p[i+1]]

def rolling(p):
    if len(find_valleys(p)) > 0:
        v = min(find_valleys(p))
        if len(descents(p[v:])) > 0:
            m = max_descent(p[v:])
        else:
m
def descent_algo(p):
    pp = p
    i = 0
    while pp != sorted(pp):



"""lemma:  If m is the maximum descent and there exists M > m with w_i = m and w_j = N where i < j, then m+1,m+2,...,n are all to the right of m and appear in consecutive order.

pf. if any appear before m, then there must be a descent to get down to m since m is a descent, so none can be before.  Therefore they are all after, again if they are not in consecutive order then a descent must appear to get to all of them."""


def remove(p, q):
    return [i for i in p if i not in q]
def sequence(a, p, i):
    for j in p:
        a[j-1] = i
    return a

def remover(pp):
    mn = index_max_descent(pp)
    m = max_descent(pp)
    try:
        M = min([j for j in pp[mn:] if j > m])
        MN = pp.index(M)
    except:
        MN = len(pp)
    pq = pp[mn:MN]

    valleys = find_valleys(pq)

    if len(valleys) == 0:
        return pq
    else:
        v = min(valleys)
        des_v = descents(pq[v:])

        if len(des_v) > 0:
            return remover(pq, a, i)
        else:
            climbs = [j for j in pq[v:] if bisect_right(pq[v-1::-1], j) != 0]
            if climbs == []:
                return pq
            else:
                j = min(climbs)
                return [i for i in pq if (i < j)]



p = [4,2,1,3]
pp = p
i = 0
a = [0 for i in sorted(p)]
remover(p)
