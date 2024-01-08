n=int(input())
sum = 99999
for i in range(n//3+1):
    for j in range(n//5+1):
        if 3*i+5*j == n:
            if i+j <= sum:
                sum = i+j

print(sum if sum!=99999 else -1)
