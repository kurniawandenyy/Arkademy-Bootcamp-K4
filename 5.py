def triangle(angka):
    string = ""
    bar=angka
    while bar >=0:
        kol = bar
        while kol >=0:
            string = string + " "
            kol = kol-1
        kanan = 1
        while kanan < (angka-(bar-1)):
            string = string + "*"
            kanan = kanan + 1
        string = string + "\n"
        bar = bar-1
    print(string)

triangle(5)