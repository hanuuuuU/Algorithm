a,b=map(int,input().split())
l=[0]
for i in range(b+1):
    for _ in range(i):
        l.append(i)
print(sum(l[a:b+1]))