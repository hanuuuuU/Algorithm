N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

mn = 1000000000
for i in range(N-T+1):
    x = 0
    for j in arr[i:i+T]: 
        x+=abs(H-j)
    mn = min(mn,x)
print(mn)