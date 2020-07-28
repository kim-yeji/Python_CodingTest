import sys
sys.stdin=open("input.txt","rt")

n, limit = map(int,input().split())
people=list(map(int,input().split()))

people.sort()

cnt=0
while people: #list자료구조가 다 비워지면 멈춘다.
    if len(people)==1: # 사람이 혼자 남을 때, 뒤에 논리 모순을 방지하기 위해!
        cnt+=1
    if people[0]+people[-1]>limit: #limit 넘어가므로 가장 무거운 사람은 혼자 타야함
        p.pop()
        cnt+=1
    else:
        people.pop(0)
        people.pop()
        cnt+=1

print(cnt)