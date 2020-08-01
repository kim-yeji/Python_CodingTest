import sys
from collections import deque
sys.stdin=open("input.txt","rt")

n, k = map(int,input().split())
deq=list(range(1,n+1)) #list에 1~n+1까지 초기화 시킨것
deq=deque(deq)

while deq:
    for _ in range(k-1):
        current=deq.popleft() #deque의 맨 앞을 pop하는 것
        deq.append(current)
    deq.popleft()
    if len(deq)==1: #큐에 자료 하나 있으므로 그냥 출력
        print(deq[0])
        deq.popleft()


