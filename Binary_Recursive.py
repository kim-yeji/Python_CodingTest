import sys
sys.stdin=open("input.txt","rt")



def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')
        
#'만일 이 파일이 인터프리터에 의해서 실행되는 경우라면'

#요약하자면 해당 모듈이 직접 실행되는 경우에는 __name__ 은 __main__ 으로 설정되어 if문 아래를 실행하지만, 
#외부에서 실행된 경우에는 __name__ 이 __main__이 아니기 때문에 if문 아래를 실행하지 않는다.
if __name__=="__main__":
    n=int(input())
    DFS(n)
