for _ in range(int(input())):
    stack=[]
    line=input()
    count=0
    for i in line:
        if i=='(':
            stack.append(1)
        else:
            if not stack:
                break
            else:
                stack.pop()
        count+=1
    if stack or count!=len(line):
        print('NO')
    else:
        print('YES')