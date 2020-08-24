import sys
sys.stdin=open("input.txt","rt")

def DFS(L, sum):
    global res
    if L==n:
        if sum>res:
            res=sum
    else:
        if L+time[L] <= n+1:  # L은 현재 지점이다. time[L]는 그  상담 시간을 더해본것.
            DFS(L+time[L], sum+pay[L])
        DFS(L+1, sum)


if __name__=="__main__":
   
    n=int(input())
    time=list()
    pay=list()
    
    for i in range(n):
        a, b = map(int,input().split())
        time.append(a)
        pay.append(b)
    res = -2147
    time.insert(0,0)
    pay.insert(0,0)
    DFS(1,0)
    print(res)