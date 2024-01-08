#기본 리스트로 구현 시 시간 초과
#insert와 remove로 해결하기엔 복잡도가 큼
#스택 두 개를 활용하여 구현하면 append와 pop만을 이용하여 구현 가능

import sys
s=sys.stdin.readline().rstrip()
stk_f=[i for i in s]
stk_b=[]
for _ in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().split())
    if command[0]=='L':
        if stk_f:
            stk_b.append(stk_f.pop())
    elif command[0]=='D':
        if stk_b:
            stk_f.append(stk_b.pop())
    elif command[0]=='B':
        if stk_f:
            stk_f.pop()
    else:
        stk_f.append(command[1])
for i in stk_f:
    print(i,end="")
for i in range(len(stk_b)):
    print(stk_b.pop(),end="")