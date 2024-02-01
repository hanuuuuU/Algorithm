import sys
input=sys.stdin.readline

# 테스트 케이스의 수가 정해져있지 않기 때문에 while로 감싸야했음
while True:
    try:
        x=int(input())*(10**7)
        n=int(input())
        lego=[int(input()) for  _ in range(n)]
        lego.sort()

        res=[]
        left=0
        right=n-1
        isPossible=False
        while left<right:
            temp=lego[left]+lego[right]
            if temp==x:
                if not res:
                    res.append(lego[left])
                    res.append(lego[right])
                elif abs(res[0]-res[1])<abs(lego[left]-lego[right]):
                    res[0],res[1]=lego[left],lego[right]
                isPossible=not isPossible
                break
            elif temp<x:
                left+=1
            else:
                right-=1
        if isPossible:
            print('yes',end=' ')
            print(*res)
        else:
            print('danger')
    except:
        break