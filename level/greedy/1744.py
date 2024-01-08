import sys
m=[]
p=[]
res=0
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    if n<=0:
        m.append(n)
    elif n==1:
        res+=1
    else:
        p.append(n)
m.sort()
p.sort(reverse=True)

if len(m)%2==1:
    res+=m.pop()
for i in range(0,len(m),2):
    res+=m[i]*m[i+1]

if len(p)%2==1:
    res+=p.pop()
for i in range(0,len(p),2):
    res+=p[i]*p[i+1]


print(res)