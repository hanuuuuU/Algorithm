p=input()
p=sorted(p)
front=[]
end=[]
ex=[]
i=0
while i<len(p)-1:
    if p[i]==p[i+1]:
        front.append(p[i])
        end.append(p[i])
        i+=2
    else:
        ex.append(p[i])
        i+=1
if i==len(p)-1:
    ex.append(p[i])
if front==end and len(ex)<2:
    print(''.join(front+ex+sorted(end,reverse=True)))
else:
    print("I'm Sorry Hansoo")