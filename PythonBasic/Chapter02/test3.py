fat=int(input("지방의 그램을 입력 하세요 :"))
carb=int(input("탄수화물의 그램을 입력 하세요 : "))
prot=int(input("단백질의 그램을 입력하세요 : "))
total=fat*9+prot*4+carb*4
print("총 칼로리 : ",format(total,"3,d"),"cal")

