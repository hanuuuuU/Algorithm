n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

pset = {}
for p,a in people:
    pset[p]= 1 if a=='G' else -1
    
end = max(pos)
mx = 0
for i in sorted(pos):
    continuous = True
    tmp = 0
    for j in range(i,end+1):
        if str(j) in pset:
            tmp += pset[str(j)]
            if pset[str(i)]!=pset[str(j)]:
                continuous = False
            if tmp==0 or continuous:
                mx = max(mx,j-i)
            
print(mx)