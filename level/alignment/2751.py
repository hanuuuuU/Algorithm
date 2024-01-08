import sys
s=[]
for _ in range(int(input())):
    s.append(int(sys.stdin.readline()))
s.sort()
for i in s:
    print(i)