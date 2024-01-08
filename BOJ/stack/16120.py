s=input()
stack=[]
for i in range(len(s)):
    if len(stack)>2 and s[i]=='P' and ''.join(stack[-3:])=='PPA':
        for _ in range(2):
            stack.pop()
    else:
        stack.append(s[i])
ppap=''.join(stack)
if ppap=='P' or ppap=='PPAP':
    print('PPAP')
else:
    print('NP')