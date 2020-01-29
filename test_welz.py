from algo.welz import *
from algo.partitions import PRSK, transpose
from algo.perms import permutations

# %%
P = [[1, 3, 6, 10, 15], [2, 5, 9, 13], [4, 7, 14], [8], [11], [12]]
P = [[1], [3], [2]]
# %%
P, T, PP = chain_insertion(P, T_0(P), 5)

print("P: {},  T: {},  PP: {}".format(P, T, PP))
# %%
P, T, PP = chain_insertion(P, T, 4, PP)

print("P: {},  T: {},  PP: {}".format(P, T, PP))

P, T, PP = chain_insertion(P, T, 3, PP)

print("P: {},  T: {},  PP: {}".format(P, T, PP))

P, T, PP = chain_insertion(P, T, 2, PP)

print("P: {},  T: {},  PP: {}".format(P, T, PP))

P, T, PP = chain_insertion(P, T, 1, PP)

print("P: {},  T: {},  PP: {}".format(P, T, PP))
# %%
print(pie(P))
# %%

print(list(range(5, 2, -1)))

# %%

w = permutations([1, 2, 3, 4])

QQ = [PRSK(ww, [3,4,4,4])[0] for ww in w]
#%%
PP = []
for P in QQ:
    if P in PP:
        continue
    else:
        PP.append(P)

print(len(PP))

#%%
i = 1
for P in PP:
    print(i, P, transpose(pie(transpose(P))))
    i = i + 1
