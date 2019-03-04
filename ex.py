
#%%
from algo import *
import pandas as pd
#%%
# RSK('341')

# for p in permutations(range(1,4)):
#     print(p, desc(p))
# p = [1,2,3]
# p.reverse()
# p
# for p in permutations(range(1,4)):
#     print(p, PRSK(p[::-1]))
# RSK('111')
# c = []
# for p in permutations(range(4)):
#     if code(p) in c:
#         pass
#     else: c.append(code(p))


# for p in permutations(range(5)):
#     c = code(p); s = sum(c[1].values())
#     print(c[0], s, RSK(c[0]))

# l = []
# for p in permutations(range(1,5)):
#     l.append((p, desc(p), RSK(p)))
q_binom('q', 5,4)
#%%
q = symbols('q')


expand(q**3*q_poly(q, 2)+ 3*q**2*q_poly(q, 4) + 3*q*q_poly(q, 6) + q_poly(q, 8))

#%%
n = 5
k = 2
l = []
for p in permutations(range(1,n+1)):
    P, Q = PRSK(p, k)
    l.append((p, shape(P), P_inv(P, k), P, Q, reading_word(Q)))


coef(n, k)
# %%

df = pd.DataFrame(l, columns=['perm', 'shapes', 'inv', 'P', 'Q', 'Q_word'])

df[
    (df.shapes == (3,2))
    ].sort_values(by=['inv']).sort_values(by='P').sort_values(by='Q')

#df
#%%
P,Q = PRSK([3,5,2,1,4], 3)
print(P, P_inv(P,3))

#%%

