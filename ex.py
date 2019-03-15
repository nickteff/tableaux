%reload_ext algo
#%%
from operator import mul
from math import factorial
from algo import *
import pandas as pd
import numpy as np
#%%

#%%
q = symbols('q')


expand(q**3*q_poly(q, 2)+ 3*q**2*q_poly(q, 4) + 3*q*q_poly(q, 6) + q_poly(q, 8))

#%%

def ex_df(n, h):
    if type(h) == int:
        h=h_function(h, n)
    l = []
    for p in permutations(range(1,n+1)):
        P, Q = PRSK(p, h)
        l.append(( shape(P), P_inv(P, h), P, Q, reading_word(Q),h))
    return pd.DataFrame(
        l,
        columns=[
            'shapes',
            'inv',
            'P',
            'Q',
            'Q_word',
            'h'
        ]).sort_values(by=['inv']).sort_values(by='P').sort_values(by='Q')


# %%
df = ex_df(5, 2)


#%%

n = 6
c = coef(4, 2)
c[2][(2,2)]
#%%

q_fact('q', 4)
q_binom('q', 6,5)
perm_coefs(3, [1, 3, 3])

def permDF(n, h):
    c = [("".join([str(k)+"::" for k in p]))[:-2] for p in partitions(n)]
    df = pd.DataFrame(perm_coefs(n,h), columns=c)
    df.index.name = df.index = df.index.rename('degree')
    return df


permDF(3,[2,3,3])
permDF(3, [3,3,3])
[0,0,0], [1,1,1], [q,q,q]
permDF(4, [2,3,4,4])
permDF(4, [3,3,4,4])









df = permDF(n,h)


for n in range(3,8):
    h = list(range(n))
    for j in range(n):
        if j == 0:
            h[j] = min(3, n)
        if j == 1:
            h[j] = min(3, n)
        else:
            h[j] = min(j+2, n)
    permDF(n, h).to_csv("".join([str(k) for k in h])+".csv", sep=";")

pd.read_csv("".join([str(k) for k in [3,3,4,4]])+".csv", sep=";")

"".join([str(i) for i in h])
p = [3,2,2]

def check(n, h):
    df = permDF(n,h)
    v = [factorial(n)/np.prod(np.array([factorial(i) for i in p])) for p in partitions(n)]
    print(sum(df@v) == factorial(n))
check(5, [2,4,4,5,5])




for p in permutations([1,2,3,4]):
    print(p, code(zero_d2e(p)), RSK(code(zero_d2e(p))[0]))
