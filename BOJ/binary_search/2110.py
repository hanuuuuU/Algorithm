import sys
input=sys.stdin.readline
n,c=map(int,input().split())
wifi=[int(input()) for _ in range(n)]
wifi.sort()

start=1
end=wifi[-1]-wifi[0]
answer=0

while start<=end:
    mid=(start+end)//2
    current=wifi[0]
    count=1

    for i in range(1,n):
        if wifi[i]>=current+mid:
            count+=1
            current=wifi[i]
    if count>=c:
        answer=mid
        start=mid+1
    else:
        end=mid-1
print(answer)