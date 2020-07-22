import sys
sys.stdin=open("input.txt","r")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

a.insert(0, [0]*n) # 0번 행에 n만큼 0으로 만든 리스트를 넣어라
a.append([0]*n)  # 마지막 행에 n만큼 0으로 만든 리스트를 넣어라
for x in a:
    x.insert(0,0)
    x.append(0)
cnt=0
for i in range(1,n+1): #가장자리인 0부터 돌면 안됨.비교대상 없음
    for j in range(1,n+1):
        if all( a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)

