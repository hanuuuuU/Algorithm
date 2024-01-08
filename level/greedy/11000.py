import sys
import heapq
room=[]
table=[]
n=int(input())
for _ in range(n):
    table.append(list(map(int,sys.stdin.readline().split())))
table.sort()

for t in table:
    if room and t[0]>=room[0]:
        heapq.heappop(room)
    heapq.heappush(room,t[1])
print(len(room))