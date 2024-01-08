import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    if i<0 or i>n-1 or j<0 or j>n-1:
        return
    if visited[i][j]:
        return
    visited[i][j]=True
    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
maxNum=max(map(max,graph))
maxCount=0
visited=[]
for k in range(maxNum):
    cnt=0
    visited=[[True]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k:
                visited[i][j]=False
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                dfs(x,y)
                cnt+=1
    maxCount=max(maxCount,cnt)
print(maxCount)