import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[0]*(n+1)
cnt=0


for i in range(2,n+1):
    if a[i]==0:
        cnt+=1
        for j in range(i,n+1,i):
            a[j]=1

print(cnt)

'''
def primeNumSieve(n):
    cnt=0
    for i in range(2,n):
        if a[i]==0:
            continue
        
        for j in range(2*j,n,j=j+i):
            print(j)
            a[j]=1

    for i in range(2,n):
        if a[i]==0:
            cnt+=1

    print(cnt)
    return cnt

primeNumSieve(n)
'''