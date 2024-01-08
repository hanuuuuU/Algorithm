n=int(input())
arr=list(map(int,input().split()))
s=list(sorted(set(arr)))
dic={s[i]:i for i in range(len(s))}
for i in arr:
    print(dic[i],end=" ")

#dictionary 개념 익히기
#dictionary = {'name':'hanu', 'health':1000, 'rising_health':30.5, 'buff':False}
#중복 허용x(중복 입력 시, 가장 나중에 입력된 중복 값으로 저장됨)