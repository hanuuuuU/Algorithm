arr = list(map(int, input().split()))

arr.sort(reverse=True)

mn = 10e9
for i in range(5):
    x = arr[i]
    arr2 = arr[:i]+arr[i+1:5]
    for j in range(4):
        y1 = arr2[0]+arr2[3]
        z1 = arr2[1]+arr2[2]
        if x!=y1 and x!=z1 and y1!=z1:
            mn = min(mn,max(x,y1,z1)-min(x,y1,z1))
        
        y2 = arr2[0]+arr2[2]
        z2 = arr2[1]+arr2[3]
        if x!=y2 and x!=z2 and y2!=z2:
            mn = min(mn,max(x,y2,z2)-min(x,y2,z2))

        y3 = arr2[0]+arr2[1]
        z3 = arr2[2]+arr2[3]
        if x!=y3 and x!=z3 and y3!=z3:
            mn = min(mn,max(x,y3,z3)-min(x,y3,z3))

            
print(mn if mn!=10e9 else -1)