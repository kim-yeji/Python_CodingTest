import sys
sys.stdin=open("input.txt","rt")

n=int(input())
s=list(map(int,input().split()))

last=0 #수열의 마지막 항을 기억해야 얘보다 큰 숫자를 가져다 놓을 수 있음
lt=0
rt=n-1
str="" #답을 출력할 문자열 (LRR 이런거)
tmp=[] #빈 리스트

while lt<=rt:
    #last보다 크기만 하다면 다 후보가 될 수 있다.
    if s[lt]>last:
        tmp.append((s[lt],'L'))
    if s[rt]>last:
        tmp.append((s[rt],'R'))

    tmp.sort()
    if len(tmp)==0:
        break
    else:
        str=str+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(str))
print(str)
