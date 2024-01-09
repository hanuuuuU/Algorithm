n=int(input())
num=list(map(int,input().split()))
selected=[]
if n==1:
    num.sort()
    print(sum(num[:5]))
else:
    selected.append(min(num[0],num[5]))
    selected.append(min(num[1],num[4]))
    selected.append(min(num[2],num[3]))
    selected.sort()

    res=0
    res+=(n**2)*selected[0] + 4*(n-1)*(n-1)*selected[0]
    res+=4*2*(n-1)*selected[1]
    res+=4*selected[2]

    print(res)

# 3x3일 때
# 윗면: 1 1 1        옆면: 2 2 3
#      1 1 1  x1         1 1 2  x4
#      1 1 1             1 1 2