alphabet={}
words=[]
num_list=[]
result=0
for _ in range(int(input())):
    words.append(input())

for word in words:
    for i in range(len(word)):
        if word[i] in alphabet:
            alphabet[word[i]]+=10**(len(word)-i-1)
        else:
            alphabet[word[i]]=10**(len(word)-i-1)

for i in alphabet.values():
    num_list.append(i)
num_list.sort(reverse=True)

num=9
for i in num_list:
    result+=num*i
    num-=1
print(result)