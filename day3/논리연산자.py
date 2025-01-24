'''
1. and : 연산자를 기준으로 왼쪽과 오른쪽 값이 모두 True 일때만 True 를 반환
2. or : 연산자를 기준으로 왼쪽과 오른쪽 값 중 하나라도 True 이면 True 를 반환
3. not : 뒤에 따라오는 논리값이 True 이면 False 반환 (반대로 출력)
        True 라면 False를 False라면 True를 반환 (단항연산자 )
'''

num1 = 10
num2 = 20
num3 = 30

num_result = num1<num2 and num2 < num3
print(num_result)

num_result2 = num1>num2 and num2<num3
print(num_result2)

num_result3 = num1>num2 or num2<num3
print(num_result3)

num_result4 = num1>num2 or num2>num3
print(num_result4)

false = False
print(false)
print(not false)
print(false)

'''
빈 문자열을 선언 후
해당 문자열이 비어있다면 True를 출력하는 프로그램 만들기
'''

text = ""
print(text)
result = not text
print(result)

'''
15라는 숫자가 10 이상 20이하 인지 확인 
'''

number = 15
number_result = 10 <= number <= 20
print(number_result)


