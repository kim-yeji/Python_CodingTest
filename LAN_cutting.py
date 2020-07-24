import sys
sys.stdin=open("input.txt","rt")

#답이 될 수 있는 개수인지 판단하는 함수(그냥 그 개수 리턴)
def howMany(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n = map(int,input().split())
Line=[]
answer=0
largest=0

for i in range(k): #입력이 줄바꿈으로 들어오기 때문에 Line에 합칠 것
    tmp=int(input()) #한 줄 읽어서
    Line.append(tmp) # 고대로 append
    largest=max(largest, tmp) #제일 큰 놈을 찾기 위함


#이분탐색 시작
lt=1
rt=largest
while lt<=rt: 
    mid=(lt+rt)//2
    if howMany(mid)>=n:
        answer=mid
        lt=mid+1 #더 좋은 답을 찾아 떠나야한다~!

    else: #개수 부족 ( 길이가 기니까 짧은 범위를 버린다)
        rt=mid-1
print(answer)


