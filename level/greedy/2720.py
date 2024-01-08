import sys
cent=[25,10,5,1]
for _ in range(int(input())):
    change=int(sys.stdin.readline())
    c=[0,0,0,0]
    for i in range(4):
        c[i]=change//cent[i]
        change%=cent[i]
    print(*c)