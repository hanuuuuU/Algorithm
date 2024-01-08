s=[0]*10
n=input()
for i in range(len(n)):
    s[int(n[i])]+=1
for i in reversed(range(10)):
    if s[i]!=0:
        for _ in range(s[i]):   print(i,end="")