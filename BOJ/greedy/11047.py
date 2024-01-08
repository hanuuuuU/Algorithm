n,k=map(int,input().split())
count=0
tp=[]
for _ in range(n):
    tp.append(int(input()))
while tp:
    m=tp.pop()
    count+=k//m
    k%=m
print(count)