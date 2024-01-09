n=int(input())
point=list(map(int,input().split()))
point.sort()
print(point[(n-1)//2])