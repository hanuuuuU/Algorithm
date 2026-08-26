ability = list(map(int, input().split()))

ability.sort()

s = []

for i in range(3):
    s.append(ability[i]+ability[5-i])

print(max(s)-min(s))