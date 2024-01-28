import sys
input=sys.stdin.readline
n,m=map(int,input().split())
sticks=list(map(int,input().split()))

start=1
end=max(sticks)
res=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for stick in sticks:
        cnt+=stick//mid
    if cnt>=n:
        res=mid
        start=mid+1
    else:
        end=mid-1
print(res)