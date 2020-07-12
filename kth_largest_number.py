
import sys
sys.stdin=open("input.txt","rt")
n, k = map(int, input().split())
num = list(map(int, input().split()))

#중복제거 = set
res=set()

#카드 3장 뽑는 중
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(num[i]+num[j]+num[m])
res=list(res) #res를 list화 시킴
res.reverse()
print(res[k-1])