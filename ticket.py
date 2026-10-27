a=int(input("Yasinizi daxil edin: "))
b=input("Telebesiniz? (beli/xeyr): ")
if a<7:
    print("Bilet pulsuzdur")
elif a>65:
    print("Biletin qiymeti 4 AZN")
elif b=="beli":
    print("Biletin qimeti 5 AZN")
else:
    print("Biletin qiymeti 8 AZN")
