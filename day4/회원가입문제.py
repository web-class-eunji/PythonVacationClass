'''
아이디
비밀번호

아이디 : 여러분의 성함
비밀번호 : 1324


아이디 비번 둘다 맞다면 로그인 되었습니다.
아이디가 일치하지 않는다면 아이디 불일치
비밀번호가 틀렸다면 비밀번호 불일치
아이디 비밀번호 불일치! 회원가입 하러가기
'''

id = input("아이디를 입력해주세요 : ")
password = int(input("비밀번호를 입력해주세요 : "))

if id == "moeunji" and password == 1234:
    print("로그인 되었습니다")
elif id != "moeunji" and password == 1234:
    print("아이디 불일치")
elif id == "moeunji" and password != 1234:
    print("비밀번호 불일치")
else:
    print("아이디, 비밀번호 불일치! 회원가입 하러가기")



is_raning = input("비가오나요? (예 / 아니오) : ")
if is_raning == "예":
    print("우산을 챙기세요!")
else:
    print("우산은 필요 없습니다.")