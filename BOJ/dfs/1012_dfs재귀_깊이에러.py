import sys
sys.setrecursionlimit(10000) #런타임 에러(RecursionError) 시 두 줄 작성

def dfs(x,y):
    if x<0 or x>m-1 or y<0 or y>n-1:
        return
    if not graph[y][x]:
        return
    graph[y][x]=False
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return

for _ in range(int(input())):
    m,n,k=map(int,input().split())
    graph=[[False]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[b][a]=True
    cnt=0
    for j in range(n):
        for i in range(m):
            if graph[j][i]==True:
                cnt+=1
                dfs(i,j)
    print(cnt)