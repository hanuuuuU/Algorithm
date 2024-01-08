def dfs(x,y):
    if x<0 or x>=s or y<0 or y>=s:
        return 0
    if graph[x][y]==1:
        graph[x][y]=0
        return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
    else:
        return 0

graph=[]
s=int(input())
for i in range(s):
    graph.append(list(map(int,input())))

result=[]
for i in range(s):
    for j in range(s):
        n=dfs(i,j)
        if n>0:
            result.append(n)
result.sort()
print(len(result))
for i in result:
    print(i)