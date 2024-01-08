a,b=map(int,input().split())
count=1
while a<b:
    if str(b)[-1]=='1':
        b//=10
    elif b%2==0:
        b//=2
    else:
        break
    count+=1
if a==b:
    print(count)
else:
    print(-1)