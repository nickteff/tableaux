from bisect import bisect
import numpy as np
from sympy.combinatorics import Permutation

from algo import permutations


def partitions(n):
    """
    A simple generator of the list of integer partiions

    Parameters
    ----------
    n : int
        The int the list of partitions is needed

    Returns
    -------
    list of lists
        A list of partitions (as lists) in descending lexicographic order
    """
    p = [1 for i in range(n)] # start with the column partition
    P = [p] # intialize with p

    N = 0
    while [n] not in P: # build up until the row partition is present
        p = P[N].copy()
        l = len(p)
        q = p[-1] #grab the last entry

        # shorten the last row by 1 
        if q > 1: 
            p[-1] = q - 1 
            q = 1
        else:
            p = p[:-1] 

        # try to add a box to each of the rows and add when possible
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

def RSK(p):
    """Given a permutation p, spit out a pair of Young tableaux"""
    P = []
    Q = []

    def insert(m, n=0):
        """Insert m into P, then place n in Q at the same place"""
        for r in range(len(P)):
            if m >= P[r][-1]:
                P[r].append(m)
                Q[r].append(n)
                return
            c = bisect(P[r], m)
            P[r][c], m = m, P[r][c]
        P.append([m])
        Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i + 1)
    return (P, Q)

def reading_word(P):
    return [item for sublist in P for item in sublist]

def shape(P):
    return tuple(len(P[r]) for r in range(len(P)))

def K(n):
    """
    Generate the Kostka matrix of the number of SSYT of content (rows) and
    shape (columns).  Rows and columns ordered in reverse lexicographic order.

    Parameters
    ----------
    n : int of the size of matrix (or size of integer partitions)

    Returns
    -------
    [numpy array]
        A square matrix with entries the number of SSYT 
    """    
    coefs = {}
    inner = {tuple(q): 0 for q in partitions(n)}
    for p in partitions(n):
        coefs[tuple(p)] = inner.copy()
        # create a list of p_1 1's, p_2 2's, etc...
        seq = [[i + 1] * p[i] for i in range(len(p))]
        seq = [i for sub in seq for i in sub]
        
        q = []
        """
        this will die as n grows, but loop over perms of the content
        run the RSK alg to get a SSYT and add one for each time the
        standard reading word comes up
        """
        for perm in permutations(seq):
            if perm not in q:
                P, Q = RSK(perm)
                q.append(perm)
                if reading_word(Q) == list(range(1, n + 1)):
                    coefs[tuple(p)][shape(P)] += 1

    # turn the data into a martic
    coefs = [coefs[p][i] for p in list(coefs) for i in list(coefs[p])]
    coefs = np.array(coefs).reshape(len(inner), len(inner)).T
    return coefs

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def max_P(P):
    return max(max(P[r]) for r in range(len(P)))


def min_P(P):
    return min(min(P[r]) for r in range(len(P)))


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


def h_banded_function(i, n):
    """
    A quick tool to get the banded h_functions

    Parameters
    ----------
    i : [type]
        [description]
    n : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return [min(j + i, n) for j in range(n)]


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
    """
    Returns the inversions of a tableau

    Parameters
    ----------
    P : [type]
        [description]
    h : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
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