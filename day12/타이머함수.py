import time

def timer(second,callback):
    print(callback)
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    print(callback)
    #time.sleep : time모듈에 들어있는 기능 (프로그램을 일정 시간동안 멈추게 하는 함수)
    print("타이머종료")


def hello():
    print("5초 뒤 실행될 함수입니다.")

timer(5,hello)

