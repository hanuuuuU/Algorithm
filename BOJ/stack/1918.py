s=list(input())
answer=[]
stack=[]
lead=False
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        answer.append(i)
    else:
        if not stack:
            stack.append(i)
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                answer.append(stack.pop())
            stack.pop()
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                answer.append(stack.pop())
            stack.append(i)
        else:
            while stack and stack[-1]!='(':
                answer.append(stack.pop())
            stack.append(i)
print(''.join(answer+stack[::-1]))