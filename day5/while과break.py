'''
시작 숫자는 : 0
숫자는 30까지 증가할것
5의 배수는 출력하지 않으며, 짝수도 출력하지 않는다.
27전까지만 출력할것이다.
break,continue 둘 다 사용하기
'''

number = 0
while number < 30:
    number += 1
    if number % 5 == 0:
        continue
    if number % 2 == 0:
        continue
    elif number > 27:
        break
    print(number)

