import sys
sys.stdin=open("input.txt","rt")

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and board[xx][yy]>board[x][y]:
                DFS(xx, yy)





if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    max=-2147
    min=2147
    cnt=0
    # 2차 배열의 최솟값과 최댓값 구하기 -> 한줄씩 읽으며 스왑한다. 

    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in range(n):
            if tmp[j] < min:
               min=tmp[j]
               sx=i #start x : 출발 지점의 x좌표
               sy=j #start y : 출발 지점의 y좌표
            if tmp[j]>min:
                max=tmp[j]
                ex=i #end x : 도착 지점의 x좌표
                ey=j #end y : 도착 지점의 y좌표
            board[i][j]=tmp[j] #이제야 board에 넣음!!
    
    DFS(sx, sy)
    print(cnt)