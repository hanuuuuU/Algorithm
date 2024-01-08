n = int(input())
for i in range(n):
    k = int(input())
    l = []
    while k > 1:
        l.append(k%2)
        k = k//2
    l.append(k)
    for idx in range(len(l)):
        if l[idx] == 1:
            print(idx,end=" ")