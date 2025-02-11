'''
1. 반복적인 코드 제거 및 재사용성 향상
2. 코드의 가독성 및 유지보수 향상
3. 오류 추적 및 디버깅 용이

def 함수이름():
    코드1
    코드2
    코드3
'''

def hello():
    print("안녕하세요")
    print("저는 은지입니다.")
    print("파이썬 수업중입니다.")

hello()


print()

colors = ["red","orange","yellow","green","skyblue"]
index = 0

def change_color():
    global index
    if index >= len(colors):
        index = 0
    print(f"배경색을 {colors[index]}로 변경합니다.")
    index += 1

change_color()
change_color()
change_color()
change_color()
change_color()
change_color()

