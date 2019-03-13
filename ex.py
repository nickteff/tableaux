
#%%
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
perm(3, [3,3,3])
perm(4, [3,3,4,4])
perm(5, [3,3,4,5,5])
perm(6, [3,3,4,5,6,6])
perm(7, [3,3,4,5,6,7,7])
perm(8, [3,3,4,5,6,7,8,8])

perm(1, [1])

perm(2, [2,2])

perm(3, [2,3,3])

perm(4, [2,3,4,4])
coef(5, [2,3,4,5,5])
perm(5, [2,3,4,5,5])
partitions(5)
perm(6, [2,3,4,5,6,6])
partitions(7)
perm(7, [2,3,4,5,6,7,7])

d =
for i in d:
    print()
c = [2,3,5,1,4,7,6]

for p in permutations([1,2,3,4]):
    print(p, code(zero_d2e(p)), RSK(code(zero_d2e(p))[0]))
