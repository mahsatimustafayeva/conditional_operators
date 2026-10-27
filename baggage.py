weight=float(input("Camadanin cekisini daxil edin(kq): "))
ticket=input("Biletin novunu daxil edin (eonom/business): ")
if weight>32:
    print("Camadan qebul edilmir")
if ticket=="econom":
    if weight<=23:
        print("Camadan pulsuzdur")
    elif weight>23 and weight<32: 
        print("Camadanin qiymeti 30 AZN")
elif ticket=="business":
    print("Camadan pulsuzdur")
else:
    print("Yanlis bilet novu")
