def dfs(n,total,add,sub,mul,div):
    global mx,mn
    if n==N:
        mx=max(mx,total)
        mn=min(mn,total)
        return
    if add:
        dfs(n+1,total+num[n],add-1,sub,mul,div)
    if sub:
        dfs(n+1,total-num[n],add,sub-1,mul,div)
    if mul:
        dfs(n+1,total*num[n],add,sub,mul-1,div)
    if div:
        dfs(n+1,int(total/num[n]),add,sub,mul,div-1)


N=int(input())
num=list(map(int, input().split()))
l=list(map(int, input().split()))
mx=int(-1e9)
mn=int(1e9)
dfs(1,num[0],l[0],l[1],l[2],l[3])

print(mx,mn,sep='\n')