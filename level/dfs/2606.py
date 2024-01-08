from collections import deque
def dfs(v):
    dfs_visited[v]=True
    for i in range(1,n+1):
        if graph[v][i] and not dfs_visited[i]:
            dfs(i)

n=int(input())
graph=[[False]*(n+1) for _ in range(n+1)]
for i in range(int(input())):
    x,y=map(int,input().split())
    graph[x][y]=True
    graph[y][x]=True
dfs_visited=[False]*(n+1)
cnt=0
dfs(1)
print(dfs_visited.count(True)-1)