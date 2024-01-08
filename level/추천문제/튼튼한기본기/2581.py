m=int(input())
n=int(input())
l=[]
if m==1: m+=1
for i in range(m,n+1):
    isPrime = True
    for j in range(2,i):
        if i%j==0:
            isPrime = False
            break
    if isPrime:
        l.append(i)
if len(l)==0:
    print('-1')
else:
    print(sum(l))
    print(l[0])