timer=[300,60,10]
s=int(input())
res=[0,0,0]
if s%10!=0:
    print(-1)
else:
    for i in range(3):
        res[i],s=divmod(s,timer[i])
    print(*res)