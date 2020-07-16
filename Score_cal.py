import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
answer = 0
cnt = 0
for i in range(n):
    if a[i] == 1:
        cnt+=1
        a[i] = cnt
    elif a[i] == 0:
        cnt = 0
        a[i] = cnt

print(sum(a))
 #unindent does not match any outer indentation level : 들여쓰기 잘못됨
 #들여쓰기를 할 때 처음에 탭 간격을 이용했으면 들여쓰기를 하는 부분 끝까지 탭을 이용해야하고, 처음에 스페이스 간격을 이용했으면 끝까지 스페이스 간격만 이용해야한다



 #답

     
    '''
    sum = 0
    cnt = 0
    for x in a:
        if x == 1:
            cnt+=1
            sum+=cnt
        else:
            cnt = 0
    '''    