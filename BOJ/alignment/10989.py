import sys
s=[0]*10001
for _ in range(int(input())):
    a = int(sys.stdin.readline())
    s[a]+=1
for i in range(len(s)):
    if s[i]!=0:
        for _ in range(s[i]):
            print(i)