import sys
sys.stdin=open("input.txt","rt")


n=int(input())
a=list(map(int,input().split()))



def reverse(x):
    result=0
    while x>0 :
        t=x%10
        result=result*10 + t # 앞자리에 0이 올 때를 무시하게 하는 부분
        x=x//10
    return result




def isPrime(x):
    if x==1:
        return False

    for i in range(2,x//2): #소수는 그 숫자의 절반에 해당하는 수까지가 본인을 제외한 수 중 젤 큰 약수임
        if x%i==0:
            return False
    else:
        return True


for i in a:
    tmp=reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')
