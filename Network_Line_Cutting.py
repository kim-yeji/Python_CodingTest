import sys
sys.stdin=open("input.txt","rt")

n=int(input())
dy=[0]*(n+1) #index 0번은 버리고 1부터 n까지 사용할 것임~!
dy[1]=1
dy[2]=2

for i in range(3,n+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[n])

