'''
사용자에게 키와 나이를 입력받을것
키가 120이상, 나이가 10살 이상이어야만 놀이기구를 탈 수 있다.

놀이기구를 탈 수 있나요? True / False
'''

height = int(input("키를 입력하세요(cm) : "))
age = int(input("나이를 입력하세요 : "))
can_ride = height >= 120 and age >= 10
print(f"놀이기구를 탈 수 있나요?{can_ride}")
print("놀이기구를 탈 수 있나요?",can_ride)

