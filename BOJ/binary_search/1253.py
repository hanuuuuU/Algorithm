n=int(input())
nums=sorted(list(map(int,input().split())))
good=0

for i in range(n):
    goal=nums[i]
    l=nums[:i]+nums[i+1:]
    start,end=0,n-2
    while start<end:
        s=l[start]+l[end]
        if s==goal:
            good+=1
            break
        elif s>goal:
            end-=1
        else:
            start+=1
print(good)