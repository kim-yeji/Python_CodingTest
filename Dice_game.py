import sys
sys.stdin=open("input.txt","rt")

result=0
n=int(input())
for i in range(n):
    tmp=input().split() #문자화 된 숫자
    tmp.sort() #정렬해서
    a, b, c =map(int,tmp) #맵핑하기
    if a==b and b==c:
        money=10000+(a*1000)
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100

    if money>result:
        result=money

print(result)