'''
딕셔너리 : 키와 쌍으로 이루어진 데이터 구조

key1 : value1,
key2 : value2
'''
from traceback import print_tb

me = {
    "name" : "MoEunJi",
    "age" : 20, # 숫자나 불리언 값은 따옴표 없이 사용 가능
    "phone" : "010-1234-5678",
    "class" : ["c언어","python","java"] # 값을 리스트로도 가질 수 있다.
}

print(me)
print(me["phone"])
print(me["class"][0])

#폰에 대한 딕셔너리
# 키 : name / price / color / storage

my_phone = {
    "name" : "아이폰16",
    "price" : "1,400,000",
    "color" : "white",
    "storage" : "256GB"
}

print(my_phone["color"])

friends = {}
friends["도현"] = 19
friends["길동"] = 27
print(friends)

print(friends["길동"])

friends["도현"] = 29
print(friends)

del friends["길동"]
print(friends)

friends.clear()
print(friends)

