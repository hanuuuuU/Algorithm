import sys
n,m=map(int,input().split())
cnt=0
s=[]
for _ in range(n):
    s.append(input())
dic={s[i]:i for i in range(n)}
for _ in range(m):
    if sys.stdin.readline().rstrip() in dic:
        cnt+=1
print(cnt)