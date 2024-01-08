s=input()
res=0
stack=[]
temp=[]
t=0
isPlus=1
for i in s:
    if i=='-':
        temp.append(int(''.join(stack))*isPlus)
        stack.clear()
        while temp:
            t+=temp.pop()
        res+=t
        isPlus=-1
        t=0
    elif i=='+':
        temp.append(int(''.join(stack))*isPlus)
        stack.clear()
    else:
        stack.append(i)
if stack:
    temp.append(int(''.join(stack))*isPlus)
res+=sum(temp)
print(res)