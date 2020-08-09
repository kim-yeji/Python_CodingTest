import sys
sys.stdin=open("input.txt","rt")


def DFS(L, subSum): #L:Level, a리스트의 인덱스를 사용 하냐 안하냐
    if subSum>total//2:
        return
    if L==n: #인덱스를 0번부터 넣었기 때문에 L이 되면 종료
        if subSum == (total-subSum):
            print("YES")
            sys.exit(0) #함수가 종료되는게 아니라 프로그램 자체를 종료시킴

    else:
        DFS(L+1, subSum + a[L]) #a[L]원소를 사용하겠다.
        DFS(L+1, subSum)        #a[L]원소를 사용하지 않겠다.
    


if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    subSum=0
    DFS(0, 0)
    print("NO")
