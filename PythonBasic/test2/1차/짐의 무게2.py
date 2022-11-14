weight=int(input("짐의 무게는 얼마입니까? "))

var=weight//10

if var>=1:
    print(f"수수료는 {var*10000}원 입니다.")
else:
    print("수수료는 없습니다.")