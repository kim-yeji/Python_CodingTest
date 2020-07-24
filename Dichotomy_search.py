import sys
sys.stdin=open("input.txt","rt")


n, m = map(int,input().split())
a= list(map(int, input().split()))
a.sort()

lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1) #0번부터 시작하는 인덱스니까
        break
    elif a[mid]>m: #큰 범위 다 날리기
        rt=mid-1
    else:
        lt=mid+1 #작은범위 다 날리기
        