import sys
sys.stdin=open("input.txt","rt")


n=int(input())
a1=list(map(int,input().split()))
m=int(input())
a2=list(map(int,input().split()))

a3=a1+a2
a3=sorted(a3)
print(a3)
'''

p1=p2=0
a3=[]
while p1<n and p2<m:
    if a1[p1]<=a2[p2]:
        a3.append(a1[p1])
        p1+=1
    else:
        a3.append(a2[p2])
        p2+=1
if p1<n:
    a3=a3+a1[p1:]
if p2<n:
    a3=a3+a2[p2:]
print(a3)
'''