#-*- coding: utf-8 -*-
#���ڱ� �ȶߴ� ������ ����. �˻��غ��� �ѱ� ���ڵ��� �ȵż���� �Ѵ�.
import sys
sys.stdin=open("input.txt","rt")

T=int(input())

for t in range(T):
    n, s, e, k = map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e] #�����̽� �ѳ� ������ ��..
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))