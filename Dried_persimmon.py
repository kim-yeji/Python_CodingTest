import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    height, direc, k = map(int, input().split()) # 인덱스 번호(1~m)로 주어지기 때문에 a[height-1] 해야함
    if direc==0: # 0이면 왼쪽으로
        for _ in range(k): # k만큼 회전
            a[height-1].append(a[height-1].pop(0)) #pop: 자동으로 꺼내서 삭제하고 뒤에 있는거 앞으로 땡겨줌=> 이 pop한 값을 append로 맨뒤에 바로 넣어버리기
    else:
        for _ in range(k):
            a[height-1].insert(0, a[height-1].pop()) # pop() : 맨 뒤에 있는거 꺼냄 , pop(0): 맨 앞에 있는거 꺼냄

            
total=0
s=0 #start
e=n-1 #end

for i in range(n):
    for j in range(s,e+1):
        total+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(total)