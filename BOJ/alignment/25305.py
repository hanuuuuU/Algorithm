n,top = map(int, input().split())
score = list(map(int,input().split()))
score.sort(reverse=True)
print(score[top-1])