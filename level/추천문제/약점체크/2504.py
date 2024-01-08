s=list(input())
result=0
stack=[]
tmp=1

for i in range(len(s)):
    if s[i]=='(':
        stack.append('(')
        tmp*=2
    elif s[i]=='[':
        stack.append('[')
        tmp*=3
    elif s[i]==')':
        if not stack or stack[-1]!='(':
            result=0
            break
        if s[i-1]=='(':
            result+=tmp
        tmp//=2
        stack.pop()
    elif s[i]==']':
        if not stack or stack[-1]!='[':
            result=0
            break
        if s[i-1]=='[':
            result+=tmp
        tmp//=3
        stack.pop()
if stack:
    print(0)
else:
    print(result) 