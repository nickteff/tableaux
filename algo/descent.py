from bisect import bisect

from perms import desc, descents


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
    Identifies elements to be removed from a list based on certain conditions.

    Args:
        pp (list): The input list.

    Returns:
        list: The list of .

    """
    if pp == []:
        return pp
    N = pp.index(max(pp))
    if N == len(pp) - 1:
        return remover(pp[:-1])
    elif N > 0:
        return remover(pp[N:])
    else:  # the max is at the beginning
        valleys = find_valleys(pp)  # find the valleys in the substring
        if len(valleys) == 0:  # return the substring if no valleys
            return pp
        else:
            v = min(valleys)  # pick the first valley
            des_v = descents(pp[v:])  # look at the descents after the first valley
            if des_v != []:  # if descents then recurse
                return remover(pp[v:])
            else:  # check if the rest of permutation climbs above the descent before the valley
                climbs = [j for j in pp[v:] if (j > pp[v - 1])]
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
