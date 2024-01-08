#모노토닉 스택

import sys
n=int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
stack=[n-1]
answer=[0]*n
for i in range(n-2,-1,-1):
    while stack and nums[i]>nums[stack[-1]]:
        answer[stack.pop()]=i+1
    else:
        stack.append(i)
print(*answer)