import sys
for _ in range(int(input())):
    l = list(map(int, sys.stdin.readline().split()))
    l = sorted(l,reverse=True)
    print(l[2])