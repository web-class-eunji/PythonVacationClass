'''
영화 이름을 입력받고 영화 평점을 입력받을것! ( 1 ~ 5 )
⚠1부터 5까지의 숫자를 입력하세요!
영화 이름 의 평점 : ⭐⭐⭐
continue/break
'''

movie_name = input("영화 이름을 입력하세요 : ")
while True:
    star_input = int(input("영화 평점을 입력하세요 : "))

    if 1 <= star_input <= 5:
        print(f"{movie_name}의 평점 : " + "⭐" * star_input)
    else:
        print("❗1부터 5 사이의 숫자를 입력하세요!")
        continue

    break



