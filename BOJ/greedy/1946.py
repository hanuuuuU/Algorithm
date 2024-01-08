from sys import stdin
for _ in range(int(input())):
    n=int(stdin.readline())
    score=[list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
    score.sort()

    count=1
    mini=score[0][1]
    for i in range(1,n):
        if score[i][1]<mini:
            count+=1
            mini=score[i][1]
    print(count)