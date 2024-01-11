import sys
n = int(input())
memo = []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a *= 100
    c *= 100
    memo.append([a+b, c+d])
memo.sort()
cnt = 0
end = 0
start = 301

while memo:
    if start >1130 or start < memo[0][0]: break

    for _ in range(len(memo)):
        if start >= memo[0][0]:
            if end <= memo[0][1]:
                end = memo[0][1]
            memo.remove(memo[0])
        else:
            break
    start = end
    cnt += 1
if start <= 1130:
    print(0)
else:
    print(cnt)