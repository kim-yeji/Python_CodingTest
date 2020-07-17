import sys
sys.stdin=open("input.txt","rt")

n=int(input())
'''
for i in range(n):
    str=input()
    str=str.upper()
    size=len(str)
    for j in range(size//2):
        if str[j]!=str[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
         print("#%d YES" %(i+1))
'''

# 좀 더 파이썬답게

for i in range(n):
    str=input()
    str=str.upper()
    if str==str[::-1]: # str[::-1]는 맨 뒷자리부터 -1씩 작아지며 문자열을 거꾸로 바꿔줌
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))