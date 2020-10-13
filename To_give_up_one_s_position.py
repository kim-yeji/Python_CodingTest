동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
def solution(동물, 자리):
    의자 =[]*자리
    answer=0


    for i in 동물:
        # 동물을 순회하면서 자리에 앉히기
        if len(의자)<3:
            if i in 의자:
                #앞에 있는 동물이 뒤로가게 됨(HIT)
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer+=1
            else:
                #나랑 다른 종인 동물이 앉아있을때
                의자.append(i)
                answer+=60
        else:
            #사람이 꽉차있을때
            if i in 의자:
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer+=1
            else:
                #자리는 꽉 차있는데 같은 종이 없다
                의자.pop(0)#최근에 아무일도 안일어난 애는 맨 앞에 있다
                의자.append(i)
                answer+=60
    
    return answer


ans = solution(동물, 3)    
hour = ans//60
minuate= ans%60

print(hour,'분', minuate,'초')