import sys
sys.stdin=open("input.txt","rt")

s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else: # ')' 라면
        stack.pop()
        if s[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)