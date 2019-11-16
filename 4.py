import re
def findpair(angka,x):
    jml = angka.count(x)
    if jml==1:
        print("Tidak Ada Pasangan")
    elif jml<1:
        print("Tidak Ada Angka", x, "dalam List")
    else:
        a = jml/2
        print ("Ada",int(a),"pasang Angka",x)

deret_angka = [1,5,5,10,9,13,5,1,5]
findpair(deret_angka,5)