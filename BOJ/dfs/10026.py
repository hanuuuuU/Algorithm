import sys
sys.setrecursionlimit(10**6)
def dfs(normal,i,j,color):
    if i<0 or i>n-1 or j<0 or j>n-1:
        return
    if normal:
        if normal_visited[i][j]:
            return
        if graph[i][j]!=color:
            return
        normal_visited[i][j]=True
    else:
        if blind_visited[i][j]:
            return
        if color=='B' and graph[i][j]!='B':
            return
        if color!='B' and graph[i][j]=='B':
            return
        blind_visited[i][j]=True
    
    dfs(normal,i-1,j,color)
    dfs(normal,i+1,j,color)
    dfs(normal,i,j-1,color)
    dfs(normal,i,j+1,color)

graph=[]
n=int(input())
for _ in range(n):
    color=sys.stdin.readline()
    graph.append(color)
count=[0,0]
normal_visited=[[False]*n for _ in range(n)]
blind_visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        color_selected=graph[i][j]
        if not normal_visited[i][j]:
            count[0]+=1
            dfs(True,i,j,color_selected)
        if not blind_visited[i][j]:
            count[1]+=1
            dfs(False,i,j,color_selected)
for i in count:
    print(i,end=' ')