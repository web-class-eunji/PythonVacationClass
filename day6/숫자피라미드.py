'''
1
22
333
4444
55555
range함수 사용 / 변수 = 5(포함시켜야함)
'''

n = 5
for i in range(1, n+1): # 12345
    for j in range(i):
        print(i, end=" ")
    print()

