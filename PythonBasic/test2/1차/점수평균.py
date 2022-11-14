point=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
tot=0
avg=0
for i in point:
    tot+=i

print(f'평균 점수 : {tot/len(point)}')