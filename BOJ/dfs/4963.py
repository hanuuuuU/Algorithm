import sys
sys.setrecursionlimit(10**6)

def dfs(di,dj):
    if di<0 or di>=b or dj<0 or dj>=a:
        return
    if visited[di][dj] or graph[di][dj]==0:
        return
    visited[di][dj]=True
    for n in range(8):
        dfs(di+graph_i[n],dj+graph_j[n])

graph_j=[0,1,1,1,0,-1,-1,-1]
graph_i=[1,1,0,-1,-1,-1,0,1]
graph=[]
visited=[]
a,b=map(int,input().split())
while a+b!=0:
    count=0
    for _ in range(b):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for _ in range(b):
        visited.append([False]*a)
    
    for i in range(b):
        for j in range(a):
            if not visited[i][j] and graph[i][j]==1:
                count+=1
                dfs(i,j)

    #다 종료 후
    print(count)
    graph.clear()
    visited.clear()
    a,b=map(int,input().split())