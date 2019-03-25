
#%%
from sympy import symbols, expand, cancel

def q_poly(q, n):
    if type(q) == str:
        q = symbols(q)
        return expand(cancel((1-q**n)/(1-q)))
    elif q == 1:
        return n
    else:
        return expand(cancel((1-q**n)/(1-q)))

def q_fact(q, n):
    if n < 2:
        return 1
    else:
        return expand(q_poly(q, n)*q_fact(q, n-1))

def q_binom(q, n, k):
    return expand(cancel(q_fact(q, n)/(q_fact(q, n-k)*q_fact(q, k))))


q = symbols("q")


expand((1+q)*(1+2*q))
