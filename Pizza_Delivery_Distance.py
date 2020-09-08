import sys
sys.stdin=open("input.txt","rt")

def DFS(L, s):
    global res
    if L==m:
        sum=0
        for i in range(len(home)):
            x1=home[i][0]
            y1=home[i][1]
            dis=2147
            for j in combination:
                x2=pizza[j][0]
                y2=pizza[j][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if res>sum:
            res=sum
    else:
        for i in range(s, len(pizza)):
            combination[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m = map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    home=[]
    pizza=[]
    combination=[0]*m #살아남을 피자집의 개수 조합
    res=2147
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                home.append((i,j))
            elif board[i][j]==2:
                pizza.append((i,j))
    DFS(0, 0)
    print(res)
