
import sys
sys.stdin=open("input.txt","rt")

n=int(input())
player=[]
for i in range(n):
    h, w= map(int,input().split())
    player.append((h,w))

player.sort(reverse=True)

cnt=0
largest=0
for h, w in player:
    if largest<w:
        largest=w
        cnt+=1
print(cnt)