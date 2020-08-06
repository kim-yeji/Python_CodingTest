import sys
import heapq as hq
sys.stdin=open("input.txt","rt")


#최대힙은 -부호를 붙여서 예를 들어 3과 4를 -3과 -4로 비교하는 것이다
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)
