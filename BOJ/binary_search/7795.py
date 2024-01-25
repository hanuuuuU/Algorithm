import sys
from bisect import bisect_right
input=sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    B=sorted(list(map(int,input().split())))
    cnt=0
    for a in A:
        cnt+=bisect_right(B,a-1)
    print(cnt)

# a가 B배열 들어갈 때 몇 번째 인덱스로 들어갈지 생각해보면
# bisect를 사용해서 찾으면됨
# bisect를 잊지말기,,