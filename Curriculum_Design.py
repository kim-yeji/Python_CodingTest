import sys
from collections import deque
sys.stdin=open("input.txt","rt")

curr=input()
n=int(input())

for i in range(n):
    plan=input()
    dq=deque(curr) #필수과목 초기화
    for x in plan: #현수가 짠 과목 하나하나 접근하는 x
        if x in dq: # x가 dq 안에 있냐?? 확인
            if x !=dq.popleft(): #일치하지 않으면 순서에 어긋난 것
                print("#%d NO" %(i+1))
                break
    else:
        #순서가 잘 통과한것 -> 그렇다고 잘 짠건 아직 모름
        if len(dq)==0: #dq가 다 비어야 순서도 맞으면서 필수과목 다 들은셈!!
            print("#%d YES" %(i+1))
                

