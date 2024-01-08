import sys
count=0
end=0
n=int(input())
sch=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sch.sort(key=lambda x:(x[1],x[0]))
for i in sch:
    if i[0]>=end:
        count+=1
        end=i[1]
print(count)