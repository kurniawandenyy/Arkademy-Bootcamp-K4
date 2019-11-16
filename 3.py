import re
def cek_kata(kata):
    list = kata.split()
    jumlah = len(list)
    jml_angka = re.findall(r'\b[a-z]{2,15}\b', kata)
    count=0
    for kata in jml_angka:
        count = count+1
    print(count,"/",jumlah)
cek_kata("ini adalah sebuah kata")
cek_kata("2 pasang sendal hilang")
