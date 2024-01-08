def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

a,b=map(int,input().split())
max = gcd(a,b)
print(max)
print(a//max*b)