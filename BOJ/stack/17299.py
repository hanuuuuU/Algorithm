n=int(input())
nums=list(map(int,input().split()))
group=[0]*1000001
stack=[]
answer=[-1]*n
for i in nums:
    group[i]+=1
for i in range(n):
    while stack and group[nums[stack[-1]]]<group[nums[i]]:
        answer[stack.pop()]=nums[i]
    stack.append(i)
print(*answer)