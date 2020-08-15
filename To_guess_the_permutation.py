import sys
sys.stdin=open("input.txt","rt")

def DFS(L,sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        print()
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__=="__main__":
    n,f = map(int,input().split())
    p=[0]*n #순열
    b=[1]*n #파스칼 이항 계수 세팅, 양쪽 맨 끝은 항상 1 이기 때문에 1로 초기화
    ch=[0]*(n+1) #순열 만들때 중복을 피하기 위한 체크배열
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0, 0)
