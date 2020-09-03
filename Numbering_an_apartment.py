import sys
sys.stdin=open("input.txt","rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x, y):
    global cnt
    cnt+=1 #하나의 좌표가 넘어오면 집개수 추가하는것
    board[x][y]=0 #카운팅 했으니까 0으로 바꿔서 중복방문을 막음
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx,yy)


if __name__=="__main__":
    n= int(input())
    board=[list(map(int,input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0 #매 단지마다 새로 덧셈해야해서 첨에 초기화하고 들어가야함
                DFS(i,j)
                res.append(cnt)
    
    print(len(res))
    res.sort()
    for x in res:
        print(x)