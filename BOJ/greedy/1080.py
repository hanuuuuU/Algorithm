n,m=map(int,input().split())
prev=[list(map(int,input())) for _ in range(n)]
answer=[list(map(int,input())) for _ in range(n)]

count=0

if (n<3 or m<3) and prev!=answer:
    count=-1
else:
    for i in range(n-2):
        for j in range(m-2):
            if prev[i][j]!=answer[i][j]:
                count+=1
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if prev[x][y]==0:
                            prev[x][y]=1
                        else:
                            prev[x][y]=0
    if prev!=answer:
        count=-1
print(count)