abilities = list(map(int, input().split()))

mn = sum(abilities)
s = sum(abilities)
for i in range(4):
    for j in range(i+1,5):
        for k in range(j+1,6):
            l = abilities[i] + abilities[j] + abilities[k]
            mn = min(mn, abs(s - 2*l))

print(mn)