#-*- coding: utf-8 -*-
#갑자기 안뜨던 오류가 떴다. 검색해보니 한글 인코딩이 안돼서라고 한다.
import sys
sys.stdin=open("input.txt","rt")

T=int(input())

for t in range(T):
    n, s, e, k = map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e] #슬라이스 넘나 간단한 것..
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))