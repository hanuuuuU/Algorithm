X,Y=map(int,input().split())
Z=Y*100//X  #int(Y/X*100)은 부동소수점 오차로 인해 오답,,,
if Z>=99:
    print(-1)
else:
    front=0
    end=X
    answer=X
    while front<=end:
        mid=(front+end)//2
        if int((Y+mid)/(X+mid)*100)>Z:
            answer=mid
            end=mid-1
        else:
            front=mid+1
    print(answer)