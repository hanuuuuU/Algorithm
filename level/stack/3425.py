import sys
l,p=map(int,input().split())
melody=[list(map(int,sys.stdin.readline().split())) for _ in range(l)]
count=0
stack=[[]for _ in range(7)]
for a,b in melody:
    if not stack[a]:
        stack[a].append(b)
        count+=1
    else:
        while stack[a] and stack[a][-1]>b:
            stack[a].pop()
            count+=1
        if stack[a] and stack[a][-1]==b:
            continue
        stack[a].append(b)
        count+=1    
print(count)