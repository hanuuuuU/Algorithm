n = int(input())
len = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans = 0
min = cost[0]
for i in range(n-1):	
	if cost[i] < min:
		min = cost[i]
	ans += min*len[i]
print(ans)