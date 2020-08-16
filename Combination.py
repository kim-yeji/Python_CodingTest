import sys
sys.stdin=open("input.txt","rt")


def DFS(L, s):
    global cnt
    if L==m:
        for i in range(L):
            print(res[i], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1) #s+1이 아니다. 가지를 뻗고 있는건 i다



if __name__=="__main__":
    n, m = map(int,input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0, 1)
    print(cnt)