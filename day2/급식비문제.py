'''
학생 한명당 필요한 급식비는 8,000원
선생님은 6,000

학생 23명과 선생님 2명이 급식을 먹는다
급식비를 계산하면?
'''

# 학생가격, 선생가격, 학생수, 선생수
student_cost = 8000
teacher_cost = 6000
student_count = 23
teacher_count = 2

teacher_total_cost = teacher_cost * teacher_count
student_total_cost = student_cost * student_count

all_cost = teacher_total_cost + student_total_cost

print("총 급식비는 : ",all_cost," 원 입니다.")