import sys
from collections import deque

sys.stdin=open("input.txt","rt")

dx=[-1,0,1,0] # 12시, 3시, 6시, 9시 방향
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
ch[n//2][n//2]=1 #중앙을 찾는다.
sum+=a[n//2][n//2] #그 중심에 있는 사과나무 개수를 일단 더하고 시작
Q.append((n//2, n//2)) 
L=0 #level 0 부터 시작
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y] ==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    '''
    print(L,size)
    for x in ch:
        print(x)
    '''
    L+=1
print(sum)
