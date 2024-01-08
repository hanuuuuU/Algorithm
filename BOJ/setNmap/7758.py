import sys
n=int(input())
dic={}
for _ in range(n):
    name,act=sys.stdin.readline().split()
    if name not in dic and act=='enter':
        dic[name]=act
    elif name in dic and act=='leave':
        del(dic[name])
sorted_key=sorted(dic,reverse=True)
for i in sorted_key:
    print(i)