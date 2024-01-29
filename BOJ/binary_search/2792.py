import sys
input=sys.stdin.readline
n,m=map(int,input().split())
gems=[int(input()) for _ in range(m)]
gems.sort()

start=1
end=gems[-1]
res=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for gem in gems:
        a,b=divmod(gem,mid)
        if b>0:
            cnt+=1
        cnt+=a
    if cnt>n:
        start=mid+1
    else:
        res=mid
        end=mid-1
print(res)