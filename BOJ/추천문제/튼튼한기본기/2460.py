max = 0
sum = 0
for _ in range(10):
    o,i = map(int, input().split())
    sum = sum - o + i
    if sum > max:
        max = sum
print(max)
    

    
