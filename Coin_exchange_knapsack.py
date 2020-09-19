import sys
sys.stdin=open("input.txt","rt")

if __name__=="__main__":

    n=int(input())
    coin=list(map(int , input().split()))
    m=int(input())
    # dy[j] : j원을 거슬러 주는데 사용된 동전의 최소 개수
    dy=[1000]*(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i],m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])
