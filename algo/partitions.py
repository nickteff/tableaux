from bisect import bisect
from itertools import accumulate, permutations, zip_longest
from typing import List, Dict, Optional, Tuple, Union


import numpy as np
import pandas as pd


class Tableau(list):
    """
    Represents a tableau, which is a nested list representing partitions.

    Inherits from the built-in list class.

    Methods:
    - reading_word(): Flatten the nested list and return a list of all the elements.
    - shape(): Returns the shape of the partition.
    - max_P(): Returns the maximum element in the tableau.
    - min_P(): Returns the minimum element in the tableau.
    - transpose(): Returns the transpose of the tableau.
    - content(): Calculates the content of the tableau.
    - locate(n): Find the row and column (using zero-based indexing) of a number in a tableau.

    Attributes:
    - P (List[List[int]]): The nested list representing the tableau.

    Example:
    >>> P = [[1, 2, 3], [4, 5], [6]]
    >>> t = Tableau(P)
    >>> t.reading_word()
    [1, 2, 3, 4, 5, 6]
    >>> t.shape()
    (3, 2, 1)
    >>> t.max_P()
    6
    >>> t.min_P()
    1
    >>> t.transpose()
    [[1, 4, 6], [2, 5], [3]]
    >>> t.content()
    (1, 1, 1, 0, 0, 0)
    >>> t.locate(4)
    (1, 0)
    """

    def __init__(self, P: List[List[int]]):
        super().__init__(P)

    def reading_word(self) -> List[int]:
        """
        Flatten the nested list P and return a list of all the elements.

        Returns:
        list: A list containing all the elements from the nested list P.
        """
        return [item for sublist in self for item in sublist]

    def shape(self) -> Tuple[int, ...]:
        """
        Returns the shape of a partition.

        Returns:
        tuple: The shape of the partition, represented as a tuple of the lengths of each row.

        Example:
        >>> P = [[1, 2, 3], [4, 5], [6]]
        >>> P.shape()
        (3, 2, 1)
        """
        return tuple(len(self[r]) for r in range(len(self)))

    def max_P(self) -> int:
        """
        Returns the maximum element in the tableau.

        Returns:
        int: The maximum element in the tableau.
        """
        return max(max(sublist) for sublist in self)

    def min_P(self) -> int:
        """
        Returns the minimum element in the tableau.

        Returns:
        int: The minimum element in the tableau.
        """
        return min(min(sublist) for sublist in self)

    def transpose(self) -> "Tableau":
        """
        Returns the transpose of the tableau.

        Returns:
        list: The transpose of the tableau.
        """
        # Transpose the tableau using zip_longest and map
        transposed = list(map(list, zip_longest(*self, fillvalue=None)))

        # Remove None values
        transposed = [[elem for elem in row if elem is not None] for row in transposed]

        return Tableau(transposed)

    def content(self) -> Tuple[int, ...]:
        """
        Calculates the content of the tableau.

        Returns:
        tuple: The content of the tableau as a tuple.
        """
        t = []
        for i in range(self.max_P() + 1):
            t.append(0)
            for r in range(len(self)):
                for c in range(len(self[r])):
                    if self[r][c] == i:
                        t[i] = t[i] + 1
        t.sort(reverse=True)  ## investigate this line -- why sort?
        return tuple(t)

    def locate(self, n: int) -> Optional[Tuple[int, int]]:
        """
        Find the row and column (using zero-based indexing) of a number in a tableau.

        Parameters
        ----------
        n : int
            The number to find.

        Returns
        -------
        tuple
            The row and column of the number in the tableau, or None if the number is not found.
        """
        for i, row in enumerate(self):
            if n in row:
                return (i, row.index(n))
        return None


def partitions(n: int) -> List[List[int]]:
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

    def generate_partitions(n: int, p: List[int]) -> Union[List[List[int]], None]:
        if n == 0:
            yield p
        else:
            for i in range(min(n, p[-1]), 0, -1):
                yield from generate_partitions(n - i, p + [i])

    return [p[1:] for p in generate_partitions(n, [n])]


def RSK(p: List[int]) -> Tuple[Tableau, Tableau]:
    """Given a permutation p, spit out a pair of Young tableaux.

    Args:
        p (list): The input permutation.

    Returns:
        tuple: A pair of Young tableaux represented as two lists, P and Q.
    """
    P = Tableau([])
    Q = Tableau([])

    def insert(m: int, n: int = 0) -> None:
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

    return P, Q


def K(n: int) -> List[List[int]]:
    """
    Generate the Kostka matrix of the number of SSYT of content (rows) and
    shape (columns).  Rows and columns ordered in reverse lexicographic order.

    Parameters
    ----------
    n : int of the size of matrix (or size of integer partitions)

    Returns
    -------
    List[List[int]]
        A square matrix with entries the number of SSYT
    """
    coefs = {}
    inner = {tuple(q): 0 for q in partitions(n)}
    for p in partitions(n):
        coefs[tuple(p)] = inner.copy()
        # create a list of p_1 1's, p_2 2's, etc...
        seq = [[i + 1] * p[i] for i in range(len(p))]
        seq = [i for sub in seq for i in sub]

        q = set()
        for perm in permutations(seq):
            perm_tuple = tuple(perm)
            if perm_tuple not in q:
                P, Q = RSK(perm)
                q.add(perm_tuple)
                if Q.reading_word() == list(range(1, n + 1)):
                    coefs[tuple(p)][P.shape()] += 1

    # turn the data into a matrix
    coefs = [[coefs[p][i] for i in coefs[p]] for p in coefs]
    coefs = [list(row) for row in zip(*coefs)]
    return coefs

def Kn(n: int) -> np.ndarray:
    """
    Generate the Kostka matrix of the number of SSYT of content (rows) and
    shape (columns). Rows and columns ordered in reverse lexicographic order.

    Parameters:
    n (int): The size of the matrix (or size of integer partitions).

    Returns:
    np.ndarray: A square matrix with entries representing the number of SSYT.
    """
    return np.array(K(n))

def Kn_inv(n: int) -> np.ndarray:
    """
    Calculate the inverse matrix of Kn(n).

    Parameters:
    n (int): The size of the matrix (or size of integer partitions).

    Returns:
    np.ndarray: The inverse matrix of Kn(n).
    """
    return np.linalg.inv(Kn(n))


def h_gen(n: int) -> List[List[int]]:
    """
    Generate all possible monotone integer sequences of length n such that
    i <= h(i) <= n.

    Args:
        n (int): The positive integer.

    Returns:
        List[List[int]]: A list of lists representing the partitions of n.

    Example:
        >>> h_gen(3)
        [[1, 2, 3], [1, 3, 3], [2, 2, 3], [2, 3, 3], [3, 3, 3]]
    """
    hh = [[i for i in range(1, n + 1)]]
    hh_set = {tuple(h) for h in hh}
    target = [n] * n

    for h in hh:
        if h != target:
            for i in range(n - 1):
                if h[i] < h[i + 1]:
                    h_new = h.copy()
                    h_new[i] += 1
                    h_new_tuple = tuple(h_new)
                    if h_new_tuple not in hh_set:
                        hh.append(h_new)
                        hh_set.add(h_new_tuple)
    return sorted(hh)


def h_banded_function(i: int, n: int) -> List[int]:
    """
    A quick tool to get the banded h_functions, i.e h(j) = min(i + j, n)

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
    return [min(j + i, n) for j in range(n+1)]


def h_bands(n: int) -> List[List[int]]:
    """
    Generate all possible banded h-functions of length n.

    Args:
        n (int): The positive integer.

    Returns:
        List[List[int]]: A list of lists representing the banded h-functions of n.

    Example:
        >>> h_bands(3)
        [[1, 2, 3], [2, 3, 3], [3, 3, 3]]
    """
    return [h_banded_function(i, n) for i in range(1, n+1)]


def h_inversions(h: List[int], p: Optional[List[int]] = None) -> List[Tuple[int, int]]:
    """
    Returns a list of inversions in a given list 'h' or a list of inversions
    in 'h' based on a permutation 'p'.

    Parameters:
    h (List[int]): The input list.
    p (List[int], optional): The permutation list. Defaults to None.

    Returns:
    List[Tuple[int, int]]: A list of inversions.

    """
    n = len(h)
    if not p:
        return [(i, j) for i in range(1,n) for j in range(i + 1, n+1) if j <= h[i-1]]
    else:
        return [(i, j) for (i, j) in h_inversions(h) if p[i-1] > p[j-1]]


def h_inv(h: List[int], p: Optional[List[int]] = None) -> int:
    """
    Calculate the number of inversions in a given list 'h' with respect to a permutation 'p'.

    Parameters:
    h (List[int]): The input list.
    p (List[int], optional): The permutation list. Defaults to None.

    Returns:
    int: The number of inversions in 'h' with respect to 'p'.
    """
    return len(h_inversions(h, p))
    


def comparable(i: int, h: List[int]) -> List[int]:
    """
    Returns a list of integers greater than h[i] from the given list h.

    Args:
        i (int): The index of the element in h.
        h (List[int]): The list of integers.

    Returns:
        List[int]: A list of integers greater than h[i].
    """
    return [j for j in range(i, len(h) + 1) if h[i - 1] < j]


def incomparable(i: int, h: List[int]) -> List[int]:
    """
    Returns a list of integers that are incomparable to the element at index i in the list h.

    Parameters:
    i (int): The index of the element in h.
    h (List[int]): The list of integers.

    Returns:
    List[int]: A list of integers that are incomparable to the element at index i in h.
    """
    return [j for j in range(i, len(h) + 1) if h[i - 1] >= j]


def check_row(row: List[int], h: List[int]) -> bool:
    """
    Check if the elements in the given row satisfy the comparison condition.

    Args:
        row (List[int]): The row to be checked.
        h (List[int]): The list of elements to compare against.

    Returns:
        bool: True if the comparison condition is satisfied, False otherwise.
    """
    for i in range(len(row) - 1):
        if row[i] in comparable(row[i + 1], h):
            return False
    return True


def check_col(col: List[int], h: List[int]) -> bool:
    """
    Check if the elements in the given column are comparable to the corresponding elements in the given list.

    Args:
        col (List[int]): The column to check.
        h (List[int]): The list of elements to compare against.

    Returns:
        bool: True if all elements in the column are comparable, False otherwise.
    """
    for i in range(len(col) - 1):
        if col[i + 1] not in comparable(col[i], h):
            return False
    return True


def gasharov(p: List[int], h: List[int]) -> List[Tableau]:
    """
    Generate Gasharov tableaux given a partition and a Hessenberg function.

    Parameters
    ----------
    p : list of int
        A partition of n.
    h : list of int
        Hessenberg function.

    Returns
    -------
    list of Tableau
        List of Gasharov tableaux satisfying the given partition and Hessenberg function.
    """
    id = list(range(1, max(h) + 1))
    p_sum = list(accumulate([0] + p))
    P = Tableau(
        [
            [i for i in range(p_sum[j - 1] + 1, p_sum[j] + 1)]
            for j in range(1, len(p) + 1)
        ]
    )
    G = []
    for w in permutations(id):
        Q = Tableau([[w[i - 1] for i in row] for row in P])
        if not any(not check_row(row, h) for row in Q):
            if not any(not check_col(col, h) for col in Q.transpose()):
                G.append((Q, P_inv(Q, h)))
    return G


def P_inv(P: Tableau, h: List[int]) -> int:
    """
    Returns the inversions of a tableau

    Parameters
    ----------
    P : list of lists
        The tableau represented as a list of lists.
    h : list
        A hessenberg function.

    Returns
    -------
    int
        The number of inversions in the tableau.
    """
    n = P.max_P()
    return [
        (i, j)
        for i in range(1, n)
        for j in incomparable(i, h)
        if P.locate(i)[1] > P.locate(j)[1]
    ]

def count_gasharov_tableaux(n: int, h: List[int]) -> Dict[int, Dict[Tuple[int, ...], int]]:
    """
    Counts the number of Gasharov tableaux for each partition and possible degree for a given h.

    Parameters
    ----------
    n : int
        The number of elements in the partition.
    h : list
        A hessenberg function.

    Returns
    -------
    dict
        A dictionary containing the counts of Gasharov tableaux for each degree and partition.
    """
    counts = defaultdict(lambda: defaultdict(int))
    for partition in partitions(n):
        tableaux = gasharov(partition, h)
        for t in tableaux:
            counts[len(t[1])][tuple(t[0].shape())] += 1
    return dict(counts)

def gasharov_df(n: int, h: List[int]) -> pd.DataFrame:
    """
    Generates a pandas DataFrame with the counts of Gasharov tableaux for each degree and partition.

    Parameters
    ----------
    n : int
        The number of elements in the partition.
    h : list
        A hessenberg function.

    Returns
    -------
    pd.DataFrame
        The DataFrame containing the counts of Gasharov tableaux.
    """
    counts = count_gasharov_tableaux(n, h)
    df = pd.DataFrame(
        data=[[counts[d][p] for p in counts[0]] for d in counts],
        columns=([str(t) for t in partitions(max(h))])
    )
    return df

def perm_gasharov_df(n: int, h: List[int]) -> pd.DataFrame:
    """
    Generates a pandas DataFrame with the counts of Gasharov tableaux multiplied by the inverse of Kn.

    Parameters
    ----------
    n : int
        The number of elements in the partition.
    h : list
        A hessenberg function.

    Returns
    -------
    pd.DataFrame
        The DataFrame containing the counts of Gasharov tableaux multiplied by the inverse of Kn.
    """
    df = gasharov_df(n, h)
    K = Kn_inv(n)
    return pd.DataFrame(df.dot(K.T), columns=df.columns)

def conjecture_checker(n: int, h_func: callable) -> Union[Tuple[int, List[int]], str]:
    """
    Checks the conjecture for a given n and a callable function for a list hessenberg functions.

    Parameters
    ----------
    n : int
        The number of elements in the partition.
    h_func : callable
        A function that returns a list of hessenberg functions.

    Returns
    -------
    Union[Tuple[int, List[int]], str]
        If the conjecture is true, returns a tuple with n and the hessenberg function.
        If the conjecture is true for all hessenberg functions, returns a string.
    """
    for h in h_func(n):
        if sum(sum(perm_gasharov_df(n, h).values)) > 0:
            return n, h
    return f"For {n}, the conjecture is true for all {h_func.__name__}."
