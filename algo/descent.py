from bisect import bisect
from algo import descents, desc


def max_descent(p):
    return max([p[i] for i in descents(p)])


def index_max_descent(p):
    return p.index(max_descent(p))


def find_valleys(p):
    return [i for i in range(1, len(p) - 1) if p[i - 1] > p[i] < p[i + 1]]


def remover(pp):
    if pp == []:
        return pp
    N = pp.index(max(pp))
    if N == len(pp) - 1:
        return remover(pp[:-1])
    elif N > 0:
        return remover(pp[N:])
    else: # the max is at the begninning
        valleys = find_valleys(pp)  # find the valleys in the substring
        if len(valleys) == 0:  # return the substring if no valleys
            return pp
        else:
            v = min(valleys)  # pick the first valley
            des_v = descents(pp[v:])  # look at the descents after the first valley
            if des_v != []:  # if descents then recurse
                return remover(pp[v:])
            else:
                climbs = [j for j in pp[v:] if (bisect(pp[v - 1::-1], j) != 0)] # note we are looking in reverse
                if climbs == []:                    
                    return pp
                else:
                    j = min(climbs)
                    return [i for i in pp if (i < j)]
            

def remove(p, q):
    return [i for i in p if i not in q]


def sequence(a, p, i):
    for j in p:
        a[j - 1] = i
    return a


def descent_algo(p):
    pp = p
    i = 0
    a = [0 for i in sorted(p)]
    deg = {i: 0 for i in range(2 * len(p))}
    while pp != sorted(pp):
        pq = remover(pp)
        d = desc(pq)
        i += 1
        deg[i] = d
        pp = remove(pp, pq)
        a = sequence(a, pq, i)
    deg = {i: deg[i] for i in deg.keys() if deg[i] != 0}
    return a, deg

"""Lemma: If m appears to the right of N in w, then a[m] > 0"""
"""Lemma: if m appears to the left of N in w, then a[m] == 0 or a[m] > a[n]"""


"""lemma:  If m is the maximum descent and there exists M > m with w_i = m and w_j = M where i < j, then m+1,m+2,...,M are all to the right of m and appear in consecutive order.

pf. if any appear before m, then there must be a descent to get down to m since m is a descent, so none can be before.  Therefore they are all after, again if they are not in consecutive order then a descent must appear to get to all of them."""
