
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
def h2(n):
    h = [i for i in range(n)]
    h[0] = 3
    for i in range(1,n):
        h[i] = min(i+2, n)
    return h

h2(4)
n = 6
coef(n, h2(n))

#%%

q_fact('q', 4)
q_binom('q', 6,5)
