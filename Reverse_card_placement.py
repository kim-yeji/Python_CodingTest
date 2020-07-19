import sys
sys.stdin=open("input.txt","rt")


card=list(range(21)) #0~20까지 리스트 만들어짐
for _ in range(10): #변수없이 반복
    s, e = map(int,input().split())
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i] #swap
        
card.pop(0)
for x in card:
    print(x, end=' ')
