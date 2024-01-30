n=int(input())
liq=sorted(list(map(int,input().split())))
left=0
right=n-1

res=[0,0]
mx=9999999999
while left<right:
    temp=liq[left]+liq[right]
    if abs(temp)<=mx:
        mx=abs(temp)
        res[0],res[1]=liq[left],liq[right]
    if temp>0:
        right-=1
    elif temp<0:
        left+=1
    else:
        break
print(*res)

# 이분탐색이 아닌 투포인터를 사용하여 해결