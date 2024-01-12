from bisect import bisect_left,bisect_right
from sys import stdin

def getCount(arr,num):
    left=bisect_left(arr,num)
    right=bisect_right(arr,num)
    return right-left

n=int(stdin.readline())
data=list(map(int,stdin.readline().split()))
m=int(stdin.readline())
nums=list(map(int,stdin.readline().split()))

data.sort()
for num in nums:
    print(getCount(data,num),end=" ")