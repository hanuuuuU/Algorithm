n=int(input())
cnt = 0
now = 666
while cnt!=n:
    if str(now).find('666')>=0:
        cnt+=1
    now+=1
print(now-1)