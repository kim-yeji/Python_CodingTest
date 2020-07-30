import sys
sys.stdin=open("input.txt","rt")

num, digit = map(int,input().split())
num=list(map(int,str(num)))
stack=[]

for x in num:
    #stack이 비어있지 않고, 지워야할 숫자의 개수가 0보다 크고, stack의 맨뒤가 x보다 작으면
    while stack and digit>0 and stack[-1]<x:
        stack.pop()
        digit-=1

    stack.append(x)

# 작은 수를 다 지우고도 digit이 남았을 때, 그 앞부분까지만 slice한다.
if digit!=0: 
    stack=stack[:-digit]

print(stack)
res=''.join(map(str, stack))
print(res)