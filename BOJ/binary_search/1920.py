n=int(input())
A=list(map(int,input().split()))
m=int(input())
X=list(map(int,input().split()))

A.sort()
for i in X:
    isin=0
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if i==A[mid]:
            isin=1
            break
        elif i<A[mid]:
            end=mid-1
        else:
            start=mid+1
    print(isin)