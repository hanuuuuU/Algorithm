import sys
input=sys.stdin.readline
n,m=map(int,input().split())
wait=[int(input()) for _ in range(n)]

res=0
start=1
end=max(wait)*m
while start<=end:
    mid=(start+end)//2
    t=0
    for i in wait:
        t+=mid//i
    if t>=m:
        res=mid
        end=mid-1
    else:
        start=mid+1
print(res)