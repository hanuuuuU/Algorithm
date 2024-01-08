import sys
import heapq
n=int(input())
cards=[int(sys.stdin.readline()) for _ in range(n)]
cards.sort()

count=0
while len(cards)>1:
        a=heapq.heappop(cards)
        b=heapq.heappop(cards)
        count+=a+b
        heapq.heappush(cards,a+b)
print(count)