import sys
sys.setrecursionlimit(10000)

def dfs(k):
    visited[k]=True
    for i in graph[k]:
        if not visited[i]:
            dfs(i)
    return

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
cnt=0
for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)
print(cnt)