 # 요소 추가하기
 # 1. add() : 한 번에 하나의 요소를 추가
 # 2. update() : 여러개의 요소를 한 번에 추가 ( 리스트나 튜플도 인자로 받아들임 )
 #
 # 요소 삭제하기
 # 1. remove() : 특정 요소 제거 ( 제거할 요소가 없으면 오류 발생 )
 # 2. discard() : 특정 요소를 제거 ( 요소가 없어도 오류 발생X)
 # 3. pop() : 임의의 요소를 제거하고 반환 ( 순서 없음 )
 # 4. clear() : 세트의 모든 요소를 제거

set = {1,2,3}
set.add(4)
print(set)

set.update({5,6})
print(set)

set_b = {"a","s","d","f","g","h","j","k","l"}
set_b.remove("a")
print(set_b)
# set_b.remove("강아지")
# print(set_b)

set_b.discard("고양이")
print(set_b)

set_red = {'r','e','d'}
print(set_red)
print(set_red.pop())
print(set_red)

set_blue = {'b','l','u','e'}
set_blue.clear()
print(set_blue)



