import random
print(">>숫자 찾추기 게임<<")

com=random.randint(1,10)

while True:
    my=int(input("예상 숫자를 입력 하시오 : "))

    if com==my:
        print("~~성공~~")
        break
    elif com>my:
        print("더 큰수를 입력")
    elif com<my:
        print("더 작은 수를 입력")
    else:
        continue