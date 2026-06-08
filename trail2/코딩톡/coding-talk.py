n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

target_u = u[p - 1]

if target_u == 0:
    print()
else:
    start_idx = p - 1
    for i in range(p - 1, -1, -1):
        if u[i] == target_u:
            start_idx = i
        else:
            break
            
    confirmed = set()
    for i in range(start_idx, m):
        confirmed.add(c[i])
        
    ans = []
    for i in range(n):
        person = chr(ord('A') + i)
        if person not in confirmed:
            ans.append(person)
            
    print(" ".join(ans))