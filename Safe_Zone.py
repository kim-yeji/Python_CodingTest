import sys
sys.stdin=open("input.txt","rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
sys.setrecursionlimit(10**6) #파이썬은 재귀함수 걸 때 시간제한을 반드시 걸어야함

def DFS(x,y,h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)

if __name__=="__main__":
    n=int(input())
    cnt=0 #안전 영역이 몇 개인가?
    res=0 #최종답
    board=[list(map(int,input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i,j,h)
        res=max(res, cnt)
        if cnt==0:
            break
    print(res)




