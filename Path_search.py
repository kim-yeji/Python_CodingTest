import sys
sys.stdin=open("input.txt","rt")

def DFS(v): #v=노드번호
    global cnt
    if v==n:
        cnt+=1
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0


if __name__=="__main__":
    n, m= map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b]=1

    cnt=0
    ch[1]=1 #1번 노드 방문했다. 하고 DFS(1)로 넘어가야함
    DFS(1)
    print(cnt)
