n=int(input())
have=list(map(int,input().split()))
m=int(input())
check=list(map(int,input().split()))

arr=list(set(have))
dic={arr[i]: 1 for i in range(len(arr))}
for i in check:
    if i in dic:
        print(1,end=" ")
    else:
        print(0,end=" ")