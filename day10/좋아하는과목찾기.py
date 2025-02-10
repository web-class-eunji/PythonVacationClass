'''
학생 딕셔너리 만들기
딕셔너리의 값이 학생들이 좋아하는 과목 리스트일것 (2가지)

어떤 과목을 좋아하는 학생을 찾을까요? - 과학

**학생이 **을(를) 좋아해요!
'''

students = {
    "철수" : ["수학","과학"],
    "영희" : ["영어","국어"],
    "민수" : ["체육","미수"],
    "지혜" : ["음악","과학"]
}

subject_input = input("어떤 과목을 좋아하는 학생을 찾을까요?")

found = False # 과목을 찾았는지 여부를 저장할 변수

for name,subject in students.items():
    if subject_input in subject:
        print(f"{name} 학생이 {subject_input}을(를) 좋아합니다!😊")
        found = True # 과목을 찾았으면 True로 변경


if not found:
    print(f"입력하신 {subject_input}은(는) 없는 과목입니다.")
