# 2343과 같은 유형의 문제

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
out=[int(input()) for _ in range(n)]

start,end = max(out),sum(out)
answer=0
while start<=end:
    mid=(start+end)//2
    temp=0
    cnt=1
    for i in out:
        if temp+i>mid:
            temp=0
            cnt+=1
        temp+=i
    if cnt<=m:
        answer=mid
        end=mid-1
    else:
        start=mid+1
print(answer)