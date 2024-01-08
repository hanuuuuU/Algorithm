import sys
n=int(input())
stack=[]
answer=[0]*n

for i in range(n):
    num=int(sys.stdin.readline())
    while stack and stack[-1][1]<=num:
        p=stack.pop()[0]
        answer[p]=i-p-1
    stack.append([i,num])

while stack:
    p=stack.pop()[0]
    answer[p]=n-p-1
print(sum(answer))