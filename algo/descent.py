from bisect import bisect
from perms import descents, desc
from mapper import mapping, code_shape, save_mapping
from math import factorial
import numpy as np
import pandas as pd
from itertools import permutations
from multiprocessing import Pool
import time

def find_valleys(p):
    """
    Finds the valleys in a given list of values.

    Args:
        p (list): A list of values.

    Returns:
        list: A list of indices where the values form a valley pattern.

    """
    return [i for i in range(1, len(p) - 1) if p[i - 1] > p[i] < p[i + 1]]

def remover(pp):
    """
    Removes elements from a list based on certain conditions.

    Args:
        pp (list): The input list.

    Returns:
        list: The modified list after removing elements.

    """
    if pp == []:
        return pp
    N = pp.index(max(pp))
    if N == len(pp) - 1:
        return remover(pp[:-1])
    elif N > 0:
        return remover(pp[N:])
    else: # the max is at the beginning
        valleys = find_valleys(pp)  # find the valleys in the substring
        if len(valleys) == 0:  # return the substring if no valleys
            return pp
        else:
            v = min(valleys)  # pick the first valley
            des_v = descents(pp[v:])  # look at the descents after the first valley
            if des_v != []:  # if no descents then recurse
                return remover(pp[v:])
            else: # check if the rest of permutation climbs above the descent before the valley
                climbs = [j for j in pp[v:] if (bisect(pp[v - 1::-1], j) != 0)] # note we are looking in reverse
                if climbs == []:                    
                    return pp
                else:
                    j = min(climbs)
                    return [i for i in pp if (i < j)]
            

def remove(p, q):
    """
    Removes elements from list p that are present in list q.

    Args:
        p (list): The list from which elements will be removed.
        q (list): The list containing elements to be removed from p.

    Returns:
        list: A new list with elements from p that are not present in q.
    """
    return [i for i in p if i not in q]


def sequence(a, p, i):
    """
    Assigns the value `i` to the elements of the list `a` at the positions specified by the list `p`.

    Args:
        a (list): The list of elements to be modified.
        p (list): The list of positions where the value `i` should be assigned.
        i (int): The value to be assigned to the specified positions.

    Returns:
        list: The modified list `a` with the assigned values.
    """
    for j in p:
        a[j - 1] = i
    return a


def descent_algo(p):
    """
    Perform the descent algorithm on a given list of integers.

    Args:
        p (list): The input list of integers.

    Returns:
        tuple: A tuple containing two elements:
            - a (list): The resulting list after performing the descent algorithm.
            - deg (dict): A dictionary containing the degrees of each step in the algorithm.
    """
    
    pp = list(p)
    i = 0
    a = [0 for _ in sorted(p)]
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

def code_shape(c):
    d = {j:0 for j in range(len(c))}
    for i in c:
        d[i] += 1
    return sorted([d[i] for i in d if d[i] > 0], reverse=True)


def worker(ww):
    code, index = descent_algo(ww)
    return [ww, str(code), str(index)]

def de_stringer(code):
    return [int(i) for i in code[1:-1].split(",")]

if __name__ == "__main__":
    for n in [8]:#range(1, 8):
        t = time.time()
        id = range(1, n+1)
        with Pool() as p:
            data = p.map(worker, permutations(id))
        df = pd.DataFrame(data, columns=['perm', 'code', 'index'])
        if n <= 8:
            df = df.assign(
                shape = df.code.apply(de_stringer).apply(code_shape)
            )
            save_mapping(df, n)
        print(n, df.loc[:, ["code", "index"]].drop_duplicates().shape[0], factorial(n), round(time.time() - t, 2))
        
   