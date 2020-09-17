import sys
sys.stdin=open("input.txt","rt")


if __name__=="__main__":
    n,m = map(int , input().split())
    print(n,"&",m)
    dy=[0]*(m+1)
    print(dy)
    print("==================================================================")
    for i in range(n):
        w, v = map(int , input().split())
        print(i,"번째 i/","무게: ",w," & ", "가치: ",v)
        for j in range(w, m+1):
            dy[j]=max(dy[j], dy[j-w]+v)
            print(j,"번째 j:", dy)
        print("==================================================================")
    print(dy[m])
