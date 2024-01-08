l = []
for _ in range(9):
    l.append(int(input()))
over = sum(l) - 100
for i in range(8):
    for j in range(i+1,9):
        if l[i]+l[j] == over:
            a = l[i]
            b = l[j]
l.remove(a)
l.remove(b)
l.sort()
for i in l:
    print(i)