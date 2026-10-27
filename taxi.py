distance=float(input("Mesafeni daxil edin: "))
hour=int(input("Saati daxil edin(0-23): "))
price=2+distance*0.80
if price<3:
    price=3
if hour>=23 or hour<=6:
    price=price*1.20
print(f"Gedis haqqi:  {price: .2f} AZN")