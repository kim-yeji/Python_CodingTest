# return 줄을 잘 맞출것!!!
# 답이 이상하게 나와서 보니까 줄 배열을 잘 안맞췄음
import sys
sys.stdin=open("input.txt","rt")

n=int(input())
num=list(map(int,input().split()))


'''
def digit_sum(x): 
    answer=0
    while(x>0):
        answer+= x%10
        x=x//10
    return answer
'''
def digit_sum(x): 
    answer=0
    for i in str(x):
        answer+=int(i)
        print(answer)
    return answer


max=-2147
for x in num:
   total=digit_sum(x)
   if total>max:
       max=total
       result=x

print(result)