import sys
sys.stdin=open("input.txt","rt")

def Count(capacity):
    cnt=1 # DVD 한 장은 꼭 필요함
    sum=0 # 음악 길이를 더해볼 것
    for x in music:
        if sum+x > capacity: # x까지 더한 값은 capacity를 초과하므로 x는 넣을 수 없음
            cnt+=1 # 새로운 DVD 필요함
            sum=x # x부터 다시 새로 저장한다.
        else:
            sum+=x
    return cnt

n,m=map(int,input().split())
music=list(map(int,input().split()))
max1 = max(music) # music중 가장 긴 노래를 찾는다.

lt=1
rt=sum(music)
answer=0

while lt<=rt:
    mid=(lt+rt)//2
    if max1<=mid and Count(mid)<=m : # DVD의 용량이 가장 긴 노래보다는 크거나 같아야한다. and 필요한 DVD 개수가 넘어옴
        answer=mid
        rt=mid-1
    else:
        lt=mid+1
print(answer)









