import sys
sys.stdin=open("input.txt","rt")

n=int(input())
meeting=[]
for i in range(n):
    start, end = map(int,input().split())
    meeting.append((start, end))
meeting.sort(key=lambda x : (x[1], x[0]))  #(x[1], x[0]) #정렬순위 정하기
'''
meeting.sort()는 원래 앞의 자료 값을 기준으로 정렬하고 그 다음에 기재된 순으로 차정렬
'''
endTime=0
cnt=0
for s, e in meeting:
    if s>= endTime:
        print(s,e)
        endTime=e
        cnt+=1
print(cnt)