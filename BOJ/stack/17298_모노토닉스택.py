# 접근법
# 1. stack에는 현재 원소를 담고 인접한 두원소끼리만 비교한다.
# 2. 인접한 두 원소 중 오른 쪽이 클때 stack을 pop하여 answer를 업데이트한다.
# 3. 그 이후에 stack의 가장위에 있는 값이 현재 오른쪽 값보다 작은 지 확인하고, 작다면 pop 한다.
# 3번은 stack이 비거나 왼쪽의 값이 더 큰 값을 가질때 까지 반복한다.
import sys
n=int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
answer=[-1]*n
stack=[0]
for i in range(1,n):
    while stack and nums[stack[-1]]<nums[i]:
            answer[stack.pop()]=nums[i]
    stack.append(i)
for i in answer:
    print(i,end=' ')


# 내가 처음 작성한 풀이(성공)
# import sys
# n=int(sys.stdin.readline().rstrip())
# nums=list(map(int,sys.stdin.readline().split()))
# stack=[[nums[0],0]]
# for i in range(1,n):
#     k=nums[i]
#     while True:
#         if stack and stack[-1][0]<k:
#             poped=stack.pop()
#             nums[poped[1]]=k
#         else:
#             break
#     stack.append([k,i])
# while stack:
#     nums[stack.pop()[1]]=-1
# nums[-1]=-1
# for i in nums:
#     print(i,end=' ')