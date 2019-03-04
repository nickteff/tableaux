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