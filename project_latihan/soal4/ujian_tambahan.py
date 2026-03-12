def sisi(a):
    hasil = a * a
    return hasil
print(sisi(5))

def angka(a, b, c):
    hasil = a + b + c
    return hasil
print(angka(1, 2, 5))

def cek_umur(a):
    if a >= 18:
        hasil = "sudah dewasa"
        return hasil
    else:
        hasil = "belum dewasa"
        return hasil
print(cek_umur(23))

def angka(a, b):
    if a > b:
        terbesar = a
        return terbesar
    else:
        terbesar = b
        return terbesar
print(angka(3, 5))
