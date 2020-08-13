import sys
sys.stdin=open("input.txt","rt")


def DFS(L, sum): # L: 동전의 사용 개수
    global answer
    if L>answer:
        return

    if sum>m:
        return

    if sum==m:
        if L<answer:
            answer=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    answer=214700
    a.sort(reverse=True) #가장 적은 동전의 개수를 구하는 것이기 때문에, 가장 큰 동전부터 사용하기위해서
    DFS(0,0)
    print(answer)
