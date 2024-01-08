s=[]
for _ in range(int(input())):
    s.append(input())
arr = list(set(s))
arr.sort
arr.sort(key=len)
for i in arr:
    print(i)