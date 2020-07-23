import sys
sys.stdin=open("input.txt","rt")

board=[list(map(int,input().split())) for _ in range(7)]
cnt=0

for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5] #0~4까지 분리(slice)
        if tmp==tmp[::-1]: #거꾸로 해서 간단하게 바로 비교(행만 가능. 같은 list)
            cnt+=1
        for k in range(2): #길이가 5이기 때문에 5/2한 몫만큼만 돌면 됨
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1

print(cnt)