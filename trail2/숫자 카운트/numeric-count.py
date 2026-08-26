n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

res = 0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or i==k or j==k:
                continue
            
            isSame = True
            for o in range(n):
                x,y,z = a[o]//100, int((a[o]/10)%10), int(a[o]%10)
                chk1 = 0
                chk2 = 0

                if i==x:
                    chk1+=1
                elif i==y or i==z:
                    chk2+=1

                if j==y:
                    chk1+=1
                elif j==x or j==z:
                    chk2+=1

                if k==z:
                    chk1+=1
                elif k==x or k==y:
                    chk2+=1

                if chk1!=b[o] or chk2!=c[o]:
                    isSame=False
                    break
            if isSame:
                res+=1
print(res)