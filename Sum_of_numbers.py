import sys
sys.stdin=open("input.txt","rt")

n,m = map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=1
cnt=0
sum=a[0] #연속적인 인덱스의 합

while True:
    if sum<m:
        if rt<n:
            sum+=a[rt]
            rt+=1
        else:  #rt==n
            break;

    elif sum==m:
        cnt+=1
        sum-=a[lt]
        lt+=1
    else:
        sum-=a[lt]
        lt+=1


print(cnt)