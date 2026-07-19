N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def chk(x,y):
    diff = abs(x-y)
    if diff <=2 or N-diff<=2:
        return 1
    return 0

cnt = 0 
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if (chk(i,a1) and chk(j,b1) and chk(k,c1)) or (chk(i,a2) and chk(j,b2) and chk(k,c2)):
                cnt+=1
print(cnt)