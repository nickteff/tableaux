from bisect import bisect
import numpy as np
from sympy.combinatorics import Permutation

from itertools import permutations


def partitions(n):
    """
    A simple generator of the list of integer partitions

    Parameters
    ----------
    n : int
        The int the list of partitions is needed

    Returns
    -------
    list of lists
        A list of partitions (as lists) in descending lexicographic order
    """
    def generate_partitions(n, p):
        if n == 0:
            yield p
        else:
            for i in range(min(n, p[-1]), 0, -1):
                yield from generate_partitions(n - i, p + [i])

    return [p[1:] for p in generate_partitions(n, [n])]

def RSK(p):
    """Given a permutation p, spit out a pair of Young tableaux.

    Args:
        p (list): The input permutation.

    Returns:
        tuple: A pair of Young tableaux represented as two lists, P and Q.
    """
    P = []
    Q = []

    def insert(m, n=0):
        """
        Insert m into P, then place n in Q at the same place

        Parameters:
        m (int): The value to be inserted into P.
        n (int, optional): The value to be inserted into Q. Default is 0.

        Returns:
        None
        """
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
    """
    Flatten the nested list P and return a list of all the elements.

    Parameters:
    P (list): A nested list representing partitions.

    Returns:
    list: A list containing all the elements from the nested list P.
    """
    return [item for sublist in P for item in sublist]

def shape(P):
    """
    Returns the shape of a partition.

    Parameters:
    P (list): The partition.

    Returns:
    tuple: The shape of the partition, represented as a tuple of the lengths of each row.

    Example:
    >>> P = [[1, 2, 3], [4, 5], [6]]
    >>> shape(P)
    (3, 2, 1)
    """
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
    """
    Calculates the content of a partition.

    Parameters:
    P (list): The partition represented as a list of lists.

    Returns:
    tuple: The content of the partition as a tuple.
    """
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
    """
    Returns a list of numbers that are incomparable to the given number 'i' in the list 'h'.

    Parameters:
    i (int): The number to compare against.
    h (list): The list of numbers.

    Returns:
    list: A list of numbers that are incomparable to 'i' in 'h'.
    """
    top = h[i - 1]
    bottom = min([j + 1 for j in range(len(h)) if h[j] >= i])
    return list(range(bottom, top + 1))


def h_banded_function(i, n):
    """
    A quick tool to get the banded h_functions

    Parameters
    ----------
    i : int
        The index of the banded function.
    n : int
        The size of the banded function.

    Returns
    -------
    list
        The banded function as a list of integers.
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
    P : list of lists
        The tableau represented as a list of lists.
    h : list
        The list of hook lengths corresponding to the tableau.

    Returns
    -------
    int
        The number of inversions in the tableau.
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