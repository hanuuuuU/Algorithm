s=[]
for _ in range(int(input())):
    a,b=input().split()
    s.append([int(a),b])
s.sort(key=lambda x:x[0])

for i in range(len(s)):
    print(s[i][0],s[i][1])