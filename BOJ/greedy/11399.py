n=int(input())
times=list(map(int,input().split()))
times.sort()
res=0
for i in range(n):
    res+=sum(times[0:i+1])
print(res)