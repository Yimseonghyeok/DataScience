multiline="""안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."""

msg=multiline.split(" ")

for i in msg:
    print(i)

print(f'단어 갯수 : {len(msg)}')