import sys, bisect
input=sys.stdin.readline
n,h=map(int,input().split())
odd=[]
even=[]
isOdd=True

for _ in range(n):
    if isOdd:
        odd.append(int(input()))
    else:
        even.append(h-int(input())) #종유석은 개똥벌레가 그냥 지나갈 수 있는 최대 높이로
    isOdd=not isOdd
odd.sort()
even.sort()

mx=n+1
size=0
for i in range(1,h+1):
    cnt=0
    cnt+=len(odd)-bisect.bisect_left(odd,i) #전체 석순에서 개똥벌레 위치보다 아래인 것들 빼서 cnt에 더하기
    cnt+=bisect.bisect_left(even,i) #개똥벌레가 이동 가능한 최대 위치보다 높다면 cnt에 더하기
    if cnt<mx:
        size=1
        mx=cnt
    elif cnt==mx:
        size+=1
        mx=cnt
print(mx,size)