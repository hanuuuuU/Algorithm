import sys
input=sys.stdin.readline
n,m=map(int,input().split())
lecture=list(map(int,input().split()))

answer=0
start,end = max(lecture),sum(lecture)
while start<=end:
    mid=(start+end)//2
    temp=0
    cnt=1
    for i in lecture:
        if temp+i>mid:
            temp=0
            cnt+=1
        temp+=i
    if cnt<=m:
        end=mid-1
        answer=mid
    else:
        start=mid+1
print(answer)