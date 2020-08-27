import sys
sys.stdin=open("input.txt","rt")

def DFS(L): # L은 인덱스다. (동전의 종류 하나하나 접근)
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha < res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha

    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1) #다음 동전으로 간다
            money[i]-=coin[L]




if __name__=="__main__":
    n=int(input())
    coin=[]
    money=[0]*3 #세 사람의 각 금액
    res=2147
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
