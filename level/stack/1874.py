from collections import deque
stack=[0]
que=deque()
answer=[]
now=1
count=0
n=int(input())
for _ in range(n):
    que.append(int(input()))
while count<n:
    if stack[-1]==que[count]:
        stack.pop()
        answer.append('-')
        count+=1
    else:
        if now>n:
            break
        stack.append(now)
        answer.append('+')
        now+=1
if count!=n:
    print('NO')
else:
    for i in answer:
        print(i)