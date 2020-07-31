import sys
sys.stdin=open("input.txt","rt")


a=input()
stack=[]
answer=''

for x in a:
    if x.isdecimal():
        answer+=x
    else: #x가 연산자임
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                answer+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                answer+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                answer+=stack.pop()
            stack.pop() # '('를 pop시킨다.
#for문이 다 돌고나서도 stack에 연산자가 남을 수 있다.
while stack:
    answer+=stack.pop()
print(answer)
