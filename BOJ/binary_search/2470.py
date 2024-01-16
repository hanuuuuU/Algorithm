n=int(input())
liq=list(map(int,input().split()))
liq.sort()
mini=9999999999
front=0
end=n-1
answer=[0,0]
while front<end:
    s=liq[front]+liq[end]
    if abs(s)<mini:
        answer[0]=liq[front]
        answer[1]=liq[end]
        mini=abs(s)

    if s<0:
        front+=1
    elif s>0:
        end-=1
    else:
        break
print(*answer)