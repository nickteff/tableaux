#%%
from bisect import bisect_right
from algo import descents, desc


def max_descent(p):
    return max([p[i] for i in descents(p)])


def index_max_descent(p):
    return p.index(max_descent(p))


def find_valleys(p):
    return [i for i in range(1, len(p) - 1) if p[i - 1] > p[i] < p[i + 1]]


def remover(pp):
    mn = index_max_descent(pp)  # location of max descent
    m = max_descent(pp)  # value of max descent
    try:
        M = min([j for j in pp[mn:] if j > m])  # value of lowest value greater than max descent
        MN = pp.index(M)  # location of above
    except:
        MN = len(pp)  # last value if nothing is bigger than max descent
    pq = pp[mn:MN]  # substring between max descent and smallest value bigger than max descent
    valleys = find_valleys(pq)  # find the valleys in the substring
    if len(valleys) == 0:  # return the substring if no valleys
        return pq
    else:
        v = min(valleys)  # pick the first valley
        des_v = descents(pq[v:])  # look at the descents after the first valley
        if des_v != []:  # if no valleys then recurse
            return remover(pq[v:])
        else:
            climbs = [j for j in pq[v:] if bisect_right(pq[v - 1::-1], j) != 0]
            if climbs == []:
                return pq
            else:
                j = min(climbs)
                return [i for i in pq if (i < j)]


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


"""lemma:  If m is the maximum descent and there exists M > m with w_i = m and w_j = N where i < j, then m+1,m+2,...,n are all to the right of m and appear in consecutive order.

pf. if any appear before m, then there must be a descent to get down to m since m is a descent, so none can be before.  Therefore they are all after, again if they are not in consecutive order then a descent must appear to get to all of them."""
