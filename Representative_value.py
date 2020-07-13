import sys
sys.stdin=open("input.txt","rt")

n=int(input())
student=list(map(int,input().split()))
min=100000
# 1.학생들의 평균 구하기
# round : round_half_even 방식은 짝수쪽으로 근사되는 값을 리턴한다. 4.5면 4로, 5.5면 6으로!
# 그래서 0.5를 더하고 int로 형변환 하면서 잘라버리는게 맞다!
average = int((sum(student) / n)+0.5)

# 2.평균에 가까운 학생 구하기
for stdNum, stdGrade in enumerate(student):# enumerate : stdNum에는 리스트의 인덱스 값을 넣고, stdGrade에는 인덱스에 해당되는 값을 넣는다.
    
    tmp = abs(stdGrade-average) #abs: 거리를 구한다 (절대값)
    if tmp<min: #거리(절대값)가 min보다 작으면
        min=tmp
        score = stdGrade
        answer=stdNum+1
# 3.중복일 경우 (1)성적 높은순 (2)학생번호가 빠른순
    elif tmp==min:
        if stdGrade>score:
            score=stdGrade
            answer=stdNum+1

print(average, answer)