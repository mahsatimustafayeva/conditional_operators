a=input("Birinci oyuncu (das/qayci/kagiz): ")
b=input("Ikinci oyuncu (das/qayci/kagiz): ")
if (a not in ["das","qayci","kagiz"]) or (b not in ["das","qayci","kagiz"]):
    print("Bele secim yoxdur")
elif a==b:
    print("Hec-hece")
elif (a=="das" and b=="qayci") or (a=="qayci" and b=="kagiz") or (a=="kagiz" and b=="das"):
    print("Birinci oyuncu qalibdir")
else:
    print("Ikinci oyuncu qalibdir")