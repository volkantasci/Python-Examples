x = int(input("İstenilen Aralığın Sonu: "))
print("1") # 1'de asal sayıdır ve direkt bastırılabilir.

for a in range(2,x):
    flag = True
    for b in range(2,a):
        if a % b == 0:
            flag = False
    if flag:
        print(a)
