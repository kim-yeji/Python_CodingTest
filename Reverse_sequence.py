import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=list(map(int,input().split()))
answer=[0]*n
for i in range(n):
    for j in range(n):
        # 자기자리 찾아 들어감
        if a[i]==0 and answer[j]==0:
            answer[j]=i+1
            break
        elif answer[j]==0: 
            a[i]-=1

for x in answer:
    print(x)
        
