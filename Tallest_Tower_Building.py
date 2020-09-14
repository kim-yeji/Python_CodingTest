import sys
sys.stdin=open("input.txt","rt")

if __name__=="__main__":
    n=int(input())
    brick=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        brick.append((a,b,c))
    brick.sort(reverse=True)
    # dy배열: 0~n번까지 벽돌들을 하나씩 살펴보면서
    #         각각의 벽돌이 꼭대기에 있을 때 가장 높이 쌓을 수 있는 깅리
    dy=[0]*n
    dy[0]=brick[0][1]
    res=brick[0][1]
    for i in range(1,n):
        max_h=0
        for j in range(i-1,0,-1):
            if brick[j][2]>brick[i][2] and dy[j]>max_h:
                max_h=dy[j]
        dy[i]=max_h+brick[i][1]
        res=max(res, dy[i])
    print(res)

