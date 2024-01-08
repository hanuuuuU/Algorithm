import sys
n = int(input())
l = list(map(int, sys.stdin.readline().split()))
cnt=0
for i in l:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
                break
    else:
        cnt+=1
print(n-cnt)