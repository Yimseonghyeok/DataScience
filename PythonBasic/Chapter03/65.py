cnt = tot =0
while cnt<5:
    cnt +=1
    tot +=cnt
    print(cnt,tot)

cnt = tot =0
dataset=[]

while cnt<100:
    cnt += 1
    if cnt%3 ==0:
        tot += cnt
        dataset.append(cnt)

print(f'1-100 사이 3의 배수 합={tot}')
print(f'dataset={dataset}')