import random

names=['홍길동','이순신','유관순']

print(names)

print(names[2])

if '유관순' in names:
    print("유관순 있음")
else:
    print("유관순 없음")

idx=random.randint(0,10)

print(names[idx])

names=['김유진','문성준','박종민','송지예','양석훈','이예지','임성혁','한권제','현재봉','이현구']

print(f"축하합니다. {names[idx]}씨 전원 아이스크림 쏘세요")
