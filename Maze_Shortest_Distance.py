import sys
from collections import deque
sys.stdin=open("input.txt","rt")

board=[list(map(int,input().split())) for _ in range(7)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0))
board[0][0]=1
while Q: #Q가 다 비워질때 까지
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0: #경계선을 넘지 않고, 통로로만 갈 수 있게
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6]==0:
    print(-1)

print(dis[6][6])