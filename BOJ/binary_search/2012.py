import sys

n = int(sys.stdin.readline())
ex = [int(sys.stdin.readline()) for x in range(n)]
ex.sort()
rank = [i for i in range(1, n+1)]
result = 0
for i in range(n):
    result += abs(rank[i] - ex[i])

print(result)