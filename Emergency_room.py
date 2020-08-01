import sys
from collections import deque
sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
# val:위험도
Q=[(pos, val) for pos, val in enumerate(list(map(int,input().split())))]
# [ (0, 60), (1, 50), (2, 70), (3, 80), (4, 90) ] 이런 튜플 형태로 만든 것
Q=deque(Q)
cnt=0

while True:
    current=Q.popleft()
    #한 개라도 참이 되면 참인 any
    if any(current[1] < x[1] for x in Q):
        Q.append(current)
    else:
        cnt+=1
        if current[0]==m:
            break

print(cnt)
