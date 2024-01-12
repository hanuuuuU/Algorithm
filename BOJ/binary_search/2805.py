n,m=map(int,input().split())
trees=list(map(int,input().split()))

start=1
end=max(trees)
res=0
while start<=end:
    mid=(start+end)//2
    wood=0
    for tree in trees:
        i=tree-mid
        if i>0:
            wood+=i
    if wood>=m:
        res=max(res,mid)
        start=mid+1
    else:
        end=mid-1

print(res)