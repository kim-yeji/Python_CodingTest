#섹션2 뒤집은 소스참고한 코드 존재!! answer= answer*10 + int(x) =>0을 제외한 자연수 만들기
import sys
sys.stdin=open("input.txt","rt")

s=input()
answer=0
for x in s:
    if x.isdecimal():
        answer= answer*10 + int(x)
print(answer)
cnt=0
for i in range(1,answer+1): #소수가 아니라 약수 구하는거라 1 포함
    if answer%i==0:
        cnt+=1
print(cnt)