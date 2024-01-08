n,l=map(int,input().split())
leak=list(map(int,input().split()))
fixed=[False for _ in range(n)]
leak.sort()

count=0
for i in range(n-1):
    if not fixed[i]:
        for j in range(n-1,i-1,-1):
            if leak[j]-leak[i]<l:
                count+=1
                for k in range(i,j+1):
                    fixed[k]=True
                break
if not fixed[-1]:
    count+=1
print(count)