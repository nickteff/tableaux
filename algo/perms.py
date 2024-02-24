from sympy.combinatorics import Permutation

def excedances(p):
    """
    Given a permutation p of [n] and excedance is a number i so
    that p[i] > i.  This function calculates the list of excedances of p

    Parameters
    ----------

    p : iterable as a permutation in one-line notation

    Returns
    -------

    e : list of indices where an excedance occurs
    """
    return [i for i in range(len(p)) if int(p[i]) > int(i)]


def exc(p):
    """
    Given a permutation p of [n] an exceedance is a number i so
    that p[i] > i.  This function calculates the number of excedances of p

    Parameters
    ----------

    p : iterable as a permutation in one-line notation

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

    p : iterable as a permutation in one-line notation

    Returns
    -------

    e : list of indices where a descent occurs
    """
    return [i for i in range(len(p) - 1) if p[i] > p[i + 1]]


def desc(p):
    """
    Given a permutation p of [n] a descent is a number i so
    that p[i] > p[i+1].  This function calculates the number of descents of p

    Parameters
    ----------

    p : iterable as a permutation in one-line notation

    Returns
    -------

    e : int of the number of descents of p
    """
    return len(descents(p))


def inversions(p):
    """
    Given a permutation p of [n] an inversion occurs when i < j and
    that p[i] > p[j].  This function calculates the pairs (i,j) of inversion of p

    Parameters
    ----------

    p : iterable as a permutation in one-line notation

    Returns
    -------

    i : a list of pairs (i,j) of descents of p
    """
    return [(i, j) for i in range(len(p) - 1)
            for j in range(i, len(p)) if p[i] > p[j]]


def inv(p):
    """
    Given a permutation p of [n] an inversion occurs when i < j and
    that p[i] > p[j].  This function calculates the number of inversion of p

    Parameters
    ----------
    p : iterable as permutation in one-line notation

    Returns
    -------
    i: int of the number of inversion of p
    """
    return len(inversions(p))


def length(p):
    return len(inversions(p))


def standard_form(p):
    """
    Return the standard form of the permutation, i.e. cycles written with largest
    element first, and largest elements in increasing order.
    """
    p = Permutation(p).full_cyclic_form

    m = [max(cycle) for cycle in p]
    m.sort()

    pp = []
    for mm in m:

        for cycle in p:
            if mm in cycle:
                l = len(cycle)
                if l == 1:
                    pp.append(cycle)
                else:
                    z = cycle.index(mm)
                    cycle = [cycle[(z + i) % l] for i in range(l)]
                    pp.append(cycle)
            else:
                pass
    return pp


def foata(p, word=True):
    """
    Return the Foata transformation of p, i.e. the word p^ obtained by deleting
    parentheses from the standard cyclic form of p
    """
    if word:
        if min(p) == 1:
            p = [i - 1 for i in p]
        p = standard_form(p)
    return [i for cycle in p for i in cycle]


def inverse_foata(c):
    """
    Return the inverse of the permutation word c wtitten in standard cyclic form
    """
    if min(c) == 1:
        cc = [i - 1 for i in c]
        c = cc
    x = [i for i in range(1, len(c)) if c[i] == max(c[:i + 1])]
    x.append(0)
    x.append(len(c))
    x.sort()
    return [c[x[i[0]]:x[i[1]]] for i in zip(range(len(x) - 1), range(1, len(x)))]


def dec2exc(c):
    """
    Giving a permutation c with k descents return the permutation with k excedances
    """
    e = Permutation(inverse_foata(c)).array_form
    return [len(e) - e[len(e) - 1 - i] for i in range(len(e))]


def zero_d2e(p):
    return [i - 1 for i in dec2exc(p)]
