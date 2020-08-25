import sys
sys.stdin=open("input.txt","rt")


def DFS(L,sum):
    global res
    if L==k:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__=="__main__":
    k=int(input())
    G=list(map(int, input().split()))
    res=set()
    s=sum(G)
    DFS(0,0)
    print(s-len(res))