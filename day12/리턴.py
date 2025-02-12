'''
def 함수이름(매개변수1,매개변수2 ...)
    코드
    return 함수 밖으로 전달하고 싶은 값
'''
from day2.논리형 import result


def plus(a,b):
    return (a+b)

sum = plus(10,20)
print(sum)

def multiply(num):
    result = num * 7
    return result

print(multiply(3))


'''
7의 배수라면 True 반환
아니라면 False반환
'''

def check_divide_seven(num):
    if num % 7 == 0:
        return True
    else:
        return False

print(check_divide_seven(49))
