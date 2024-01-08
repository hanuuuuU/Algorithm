from collections import deque
def dfs(v):
    print(v,end=' ')
    dfs_visited[v]=True
    for i in range(1,n+1):
        if not graph[v][i] or dfs_visited[i]:
            continue
        dfs(i)

def bfs(start):
    queue=deque([start])
    bfs_visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if graph[v][i] and not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True


n,m,start=map(int,input().split())
graph=[[False]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)
dfs(start)
print()
bfs(start)