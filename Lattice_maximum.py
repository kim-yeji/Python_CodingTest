import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)] #2차원 리스트 선언

largest = -2147
for i in range(n):
    sum1=sum2=0 
    for j in range(n):
        sum1+=a[i][j]  #sum1: 행의 합, 
        sum2+=a[j][i]  #sum2: 열의 합
    if largest<sum1:
        largest = sum1
    if largest<sum2:
        largest = sum2

#대각선 합 구하기
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]  #대각선의 합
    sum2+=a[i][n-i-1] #역대각선의 합
if largest<sum1:
    largest = sum1
if largest<sum2:
    largest = sum2


print(largest)