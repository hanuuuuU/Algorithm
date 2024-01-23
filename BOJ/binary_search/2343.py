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

# 블루레이의 최소 크기는 한 칸씩 잘랐을 때
#         최대 크기는 하나도 안잘랐을 때
# 그 사이에서 블루레이 크기 지정하며 블루레이 개수 세기
# 만약 블루레이 개수가 목표치보다 많으면 크기를 늘려서 한 개의 블루레이에 많이 들어가도록