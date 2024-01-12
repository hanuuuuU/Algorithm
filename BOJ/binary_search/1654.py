import sys
input=sys.stdin.readline
n,k=map(int,input().split())
lan=[int(input()) for _ in range(n)]

start=1
end=max(lan)
length=0

while start<=end:
    cnt=0
    mid=(start+end)//2
    for i in lan:
        cnt+=i//mid
    if cnt>=k:
        length=max(length,mid)
        start=mid+1
    else:
        end=mid-1
print(length)