import sys
from bisect import bisect_left

input=sys.stdin.readline
m,n,l = map(int, input().split())
gun = list(map(int, input().split()))

gun.sort()
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if not y > l:
        if x <=gun[0]:
            if gun[0]-x + y <=l:
                count +=1
        elif x >= gun[-1]:
            if x-gun[-1] + y <=l:
                count +=1
        else:
            idx = bisect_left(gun, x)
            if (abs(x - gun[idx - 1])+y) <= l or (abs(gun[idx] - x)+y) <= l:
                count += 1
print(count)