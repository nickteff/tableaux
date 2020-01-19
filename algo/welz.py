# %%
import copy

from algo import transpose, max_P, min_P


def row_number(P, i):
    for row in range(len(P)):
        if i in P[row]:
            return row
        else:
            continue


def coord(P, i):
    row = row_number(P, i)
    return row, P[row].index(i)


def T_0(P):
    T = []
    for r in range(len(P)):
        T.append([])
        for c in range(len(P[r])):
            T[r].append('x')
    return T


def T_fin(T, i):
    for r in range(len(T)):
        for c in range(len(T[r])):
            if T[r][c] < 0:
                T[r][c] = T[r][c] + i
    return T


def remove(P, T, PP, i, l):
    r, c = coord(PP, i)
    T[r][c] = l
    PP[r][c] = 0
    r, c = coord(P, i)
    if len(P[r]) == 1:
        P.remove(P[r])
    else:
        P[r].remove(i)

    return P, T, PP


def chain_insertion(P, T, l, PP=None):
    if PP is None:
        PP = copy.deepcopy(P)
    # Up Phase
    N = max_P(P)
    # find M
    M = N
    while row_number(P, M) > row_number(P, M - 1):
        M = M - 1
        if M == 1:
            break
    # Down Phase
    if N == M:
        k = N
        while row_number(P, k) < row_number(P, k - 1):
            k = k - 1
            if k == 1:
                break
    if N > M:
        k = M
        while (row_number(P, k) < row_number(P, k - 1)) and (row_number(P, k - 1) < row_number(P, M + 1)):
            k = k - 1
            if k == 1:
                break
    for i in range(M, N + 1):
        P, T, PP = remove(P, T, PP, i, l)
    for i in range(M - 1, k - 1, -1):
        P, T, PP = remove(P, T, PP, i, l)

    return P, T, PP


def pie(P):
    i = 1
    if transpose(P) == [list(range(1, len(P) + 1))]:
        return [[0] for i in range(max_P(P))]
    P, T, PP = chain_insertion(P, T_0(P), -i)
    i = i + 1
    while P != [] and transpose(P) != [list(range(1, len(P) + 1))]:
        P, T, PP = chain_insertion(P, T, -i, PP)
        i = i + 1
    if P == []:
        return T_fin(T, i)
    else:
        for j in list(range(1, len(P) + 1)):
            P, T, PP = remove(P, T, PP, j, 0)

        return T_fin(T, i)
