# this code is experimental

 
def PRSK(p, h=1):
    '''Given a permutation p, spit out a pair P a P_n,k tableaux and Q a standard Young tableaux
    -- See Sundquist, Wagner, West'''
    P = []
    Q = []
    if type(h) == int:
        h = h_function(h, len(p))
    p = p[::-1]

    def insert(m, n, h):
        '''Insert m into P, then place n in Q at the same place'''
        chk = incomparable(m, h)
        for r in range(len(P)):
            if len(intersection(chk, P[r])) == 2:
                continue
            elif len(intersection(chk, P[r])) == 1:
                o = intersection(chk, P[r])[0]
                c = P[r].index(o)
                P[r][c], m = m, P[r][c]
                chk = incomparable(m, h)
                continue
            elif m > P[r][-1]:
                P[r].append(m)
                Q[r].append(n)
                return
            else:
                c = bisect(P[r], m)
                P[r][c], m = m, P[r][c]
                chk = incomparable(m, h)

        P.append([m])
        Q.append([n])

    for i in range(len(p)):
        insert(int(p[i]), i + 1, h)

    P = transpose(P)
    Q = transpose(Q)

    return (P, Q)



def coef(n, h):
    if type(h) == int:
        h = h_function(h, n)
    coefs = {i: {} for i in range(sum(range(n + 1)) + 1)}
    for p in permutations(range(1, n + 1)):
        P, Q = PRSK(p, h)
        if reading_word(Q) == list(range(1, n + 1)):
            if shape(P) in list(coefs[P_inv(P, h)].keys()):
                coefs[P_inv(P, h)][shape(P)] += 1
            else:
                coefs[P_inv(P, h)][shape(P)] = 1

    coefs = {i: coefs[i] for i in coefs.keys() if coefs[i] != {}}
    return coefs





