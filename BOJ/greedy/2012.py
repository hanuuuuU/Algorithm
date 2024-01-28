import sys
input=sys.stdin.readline
n=int(input())
nums=[int(input()) for _ in range(n)]
nums.sort()
cnt=0
for i in range(n):
    cnt+=abs(nums[i]-i-1)
print(cnt)