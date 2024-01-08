#스택 두 개
import sys
for _ in range(int(input())):
    fstack=[]
    bstack=[]
    l=sys.stdin.readline().rstrip()
    for i in l:
        if i=='<':
            if fstack:
                bstack.append(fstack.pop())
        elif i=='>':
            if bstack:
                fstack.append(bstack.pop())
        elif i=='-':
            if fstack:
                fstack.pop()
        else:
            fstack.append(i)
    for i in fstack:
        print(i,end="")
    bstack.reverse()
    for i in bstack:
        print(i,end="")
    print()