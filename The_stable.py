import sys
sys.stdin=open("input.txt","rt")


def Count(length):
    cnt=1
    endPoint=line[0] #말이 마지막으로 배치된 지점

    for i in range(1,n): # 2번째, 3번째, n번째 말들을 배치해보려고 함
        if line[i]-endPoint >= length: #말을 배치 할 수 있음
            cnt+=1
            endPoint=line[i]
    return cnt



n,c=map(int,input().split())
line=[]

for _ in range(n):
    tmp=int(input())
    line.append(tmp)

line.sort()
lt=1
rt=line[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        answer=mid
        lt=mid+1
    else:
        rt=mid-1

print(answer)
