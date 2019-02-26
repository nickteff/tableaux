from algo import RSK, PRSK, permutations, code


RSK('341')

for p in permutations(range(1,4)):
    print(p, PRSK(p))

 RSK('000')
RSK('111')
c = []
for p in permutations(range(4)):
    if code(p) in c:
        pass
    else: c.append(code(p))


for cd in c:
    print(cd[0], RSK(cd[0]), sum(cd[1].values()))
 
