print("수열 = ", end='')
tot=0
for i in range(1,101):
    if (i%3==0) and (i%2!=0):
        print(i,end=' ')
        tot+=i
print()
print(f"누적 합 : {tot}")