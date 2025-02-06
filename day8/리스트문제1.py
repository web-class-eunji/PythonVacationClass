'''
여러가지 숫자가 있는 리스트에서 5 이상인 숫자만 비어있는 리스트에 추가하고 오름차순으로 변경해서 출력
3,7,8,6,10,4,2,5,0,1
'''

# append() : 리스트 끝에 요소를 추가하는 메서드

number = [3,7,8,6,10,4,2,5,0,1]
new_list = []
for num in number:
    if num > 5:
        new_list.append(num)
new_list.sort()
print(new_list)


