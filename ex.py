from algo import *

RSK('341')

for p in permutations(range(1,4)):
    print(p, desc(p))
p = [1,2,3]
p.reverse()
p
for p in permutations(range(1,4)):
    print(p, PRSK(p[::-1]))
RSK('111')
c = []
for p in permutations(range(4)):
    if code(p) in c:
        pass
    else: c.append(code(p))


for p in permutations(range(5)):
    c = code(p); s = sum(c[1].values())
    print(c[0], s, RSK(c[0]))

for p in permutations(range(1,5)):
    print(p, desc(p), RSK(p))
