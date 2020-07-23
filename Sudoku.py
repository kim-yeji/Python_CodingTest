import sys
sys.stdin=open("input.txt","rt")

def check(a):
    for i in range(9):
        row=[0]*10  # 행 체크리스트
        col=[0]*10  # 열 체크리스트
        for j in range(9):
            row[a[i][j]]=1
            col[a[j][i]]=1
        if sum(row)!=9 or sum(col)!=9:
            return False

    for i in range(3):
        for j in range(3):
            sqr=[0]*10  # 3x3 사각형 체크리스트
            for k in range(3):
                for s in range(3):
                    sqr[a[i*3+k][j*3+s]]=1
            if sum(sqr)!=9:
                return False
    return True

        
 
a=[list(map(int,input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")