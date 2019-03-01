from bisect import bisect
import numpy as np
from sympy.combinatorics import Permutation

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

intersection([1,2,3], [2,5])
def PRSK(p, k):
    '''Given a permutation p, spit out a pair P a P_n,2 tableaux and Q a standard Young tableaux
    -- See Sundquist, Wagner, West'''
    P = []
    Q = []

    def insert(m, n=0, k=0):
            '''Insert m into P, then place n in Q at the same place'''
            chk = [m+diff for diff in range(-k+1, k)]
            for r in range(len(P)):
                if len(intersection(chk, P[r])) == 2:
                        continue
                elif len(intersection(chk, P[r])) == 1:
                    o = intersection(chk, P[r])[0]
                    c = P[r].index(o)
                    P[r][c], m = m, P[r][c]
                    chk = [m+diff for diff in range(-k+1, k)]
                    continue
                elif m > P[r][-1]:
                    P[r].append(m)
                    Q[r].append(n)
                    return
                else:
                    c = bisect(P[r], m)
                    P[r][c], m = m, P[r][c]
                    chk = [m+diff for diff in range(-k+1, k)]

            P.append([m])
            Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i+1, k)

    #P = transpose(P)
    #Q = transpose(Q)

    return (P, Q)

PRSK([1,4,3,2], 3)
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

for p in permutations(range(1,4)):
    print(p, PRSK(p, 3))

P, Q = PRSK([1,3,2], 2)

Q
j = []
for i in range(len(Q)):
    j.append(Q[i])



flat_list
j
j.append(Q[0])
j
