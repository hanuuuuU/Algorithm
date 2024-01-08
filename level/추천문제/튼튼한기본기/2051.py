import sys
M, n = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1,M+1):
    if M%i == 0:
        cnt+=1
        if cnt == n:
            print(i)
if n>cnt:
    print(0)