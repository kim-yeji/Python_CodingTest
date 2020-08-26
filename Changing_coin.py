import sys
sys.stdin=open("input.txt","rt")


def DFS(L, sum): #sum: 금액이 완성 되는것. L:1이면 5원 2면 10원 4이면 1원 이런식(인덱스)
   global cnt
   if L==k:
        if sum==t:
            cnt+=1
   else:
        for i in range(coinNum[L]+1):
            DFS(L+1, sum + (coinVal[L]*i))



if __name__=="__main__":
    t=int(input())
    k=int(input())
    coinVal=list() #동전의 금액
    coinNum=list() #동전의 개수
    for i in range(k):
        a, b = map(int, input().split())
        coinVal.append(a)
        coinNum.append(b)
    cnt=0
    DFS(0, 0)
    print(cnt)
