n=int(input())
reg=sorted(list(map(int,input().split())))
limit=int(input())

start=1
end=max(reg)
res=0
while start<=end:
    mid=(start+end)//2
    total=0
    for i in reg:
        if i<mid:
            total+=i
        else:
            total+=mid
    if total<=limit:
        res=max(res,mid)
        start=mid+1
    else:
        end=mid-1
print(res)