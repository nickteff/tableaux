from bisect import bisect
import numpy as np
from sympy.combinatorics import Permutation

p = [6,8,4,3,7,1,2,0,5]

def RSK(p):
    '''Given a permutation p, spit out a pair of Young tableaux'''
    P = []; Q = []
    def insert(m, n=0):
        '''Insert m into P, then place n in Q at the same place'''
        for r in range(len(P)):
            if m >= P[r][-1]:
                P[r].append(m); Q[r].append(n)
                return
            c = bisect(P[r], m)
            P[r][c],m = m,P[r][c]
        P.append([m])
        Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i+1)
    return (P,Q)

def permutations (orig_list):
    """
    Given a orig_list return a generator of all of the permutations of orig_list
    """
    if not isinstance(orig_list, list):
        orig_list = list(orig_list)
    yield orig_list

    if len(orig_list) == 1:
        return

    for n in sorted(orig_list):
        new_list = orig_list[:]
        pos = new_list.index(n)
        del(new_list[pos])
        new_list.insert(0, n)
        for resto in permutations(new_list[1:]):
            if new_list[:1] + resto != orig_list:
                yield new_list[:1] + resto

def excedances(p):
    """
    Given a permutation p of [n] and excedance is a number i so
    that p[i] > i.  This function calculates the list of excedances of p

    Parameters
    ----------

    p : interable as a permutation in one-line notation

    Returns
    -------

    e : list of indices where an excedance occurs
    """
    return [i for i in range(len(p)) if int(p[i]) > int(i)]


def exc(p):
    """
    Given a permutation p of [n] a descent is a number i so
    that p[i] > p[i+1].  This function calculates the number of excedances of p

    Parameters
    ----------

    p : interable as a permutation in one-line notation

    Returns
    -------

    e : int the number of excedances of p
    """
    return len(excedances(p))

def descents(p):
    """
    Given a permutation p of [n] a descent is a number i so
    that p[i] > p[i+1].  This function calculates the list of descents of p

    Parameters
    ----------

    p : interable as a permutation in one-line notation

    Returns
    -------

    e : list of indices where a descent occurs
    """
    return [i for i in range(len(p)-1) if p[i] > p[i+1]]

def desc(p):
    """
    Given a permutation p of [n] a descent is a number i so
    that p[i] > p[i+1].  This function calculates the number of descents of p

    Parameters
    ----------

    p : interable as a permutation in one-line notation

    Returns
    -------

    e : int of the number of descents of p
    """
    return len(descents(p))

def inversions(p):

    return ([(i,j) for i in range(len(p)-1)
                for j in range(i, len(p)) if p[i] > p[j]])

def inv(p):
    return len(inversions(p))

def length(p):
    return len(inversions(p))

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
    cc = []
    for c in Permutation(p).full_cyclic_form:
        if m in c:
            l = len(c)
            z = c.index(m)
            return [c[(z+i)%l] for i in range(l)]


def get_r(p):
    """
    Get the r from Stembridge's algorithm
    """
    r = 0
    c = get_cycle(p)
    while r < len(c):
        if c[r] > c[(r+1)%len(c)]:
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
    for s in range(r,len(c)):
        if c[s] > c[(s+1)%len(c)]:
            ss.append(s)
        if c[r-1] <= c[(s+1)%len(c)]:
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
    if s == l-1:
        del pp[cm]
        return Permutation(pp).array_form
    else:
        del c[1:s+1]
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
    if s == l-1:
        del pp[cm]
        p = Permutation(pp).array_form
        for i in c:
            a[i] = k+1
        f[k+1] = l - r
    else:
        for i in c[1:s+1]:
            a[i] = k+1
        if c[s] > c[(s+1)%l]:
            f[k+1] = s - r
        if c[r-1] <= c[(s+1)%l]:
            f[k+1] = s - r + 1
        del c[1:s+1]
        pp[cm] = c
        p = Permutation(pp).array_form
    return (p, a, f)


def code(p):
    """
    Calculate the marked code of a permutation
    -- See Stembridge
    """
    a = np.zeros_like(p)
    f = {0:0}
    while p != list(range(len(p))):
        p, a, f = new_triple(p, a, f)
    return list(a),f

def all_perms(n):
    """
    Iteration over all of the permutations of [n]
    """
    for p in permutations(range(n)):
        a, f = code(p)
        p = [1+i for i in p]
        print(p, RSK(a), f)


def PRSK(p):
    '''Given a permutation p, spit out a pair P a P_n,2 tableaux and Q a standard Young tableaux
    -- See Sundquist, Wagner, West'''
    P = []
    Q = []

    def insert(m, n=0):
            '''Insert m into P, then place n in Q at the same place'''
            for r in range(len(P)):
                if m-1 in P[r]:
                    if m+1 in P[r]:
                        continue
                    else:
                        c = P[r].index(m-1)
                        P[r][c], m = m, P[r][c]
                        continue
                elif m+1 in P[r]:
                    c = P[r].index(m+1)
                    P[r][c], m = m, P[r][c]
                    continue
                elif m > P[r][-1]:
                    P[r].append(m)
                    Q[r].append(n)
                    return
                else:
                    c = bisect(P[r], m)
                    P[r][c], m = m, P[r][c]

            P.append([m])
            Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i+1)

    P = transpose(P)
    Q = transpose(Q)

    return (P, Q)

def transpose(P):
    """
    Returns the transpose of a tableau
    """
    PP = []
    n = max(max(P))
    for i in range(len(P)):
        for j in range(len(P[i])):
                PP.append([j, P[i][j]])

    ind = [[i[1] for i in PP if i[0] == j] for j in range(n)]

    p = []
    for i in range(len(ind)):
        if len(ind[i]) != 0:
            p.append(ind[i])
    return p
