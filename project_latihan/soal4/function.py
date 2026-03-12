def sapa():
    print("hallo rifqi")
sapa()
sapa()

#dengan nama
nama = input("masukkan nama kamu:")
def sapa (nama):
    print("hallo", nama)
sapa(nama)

#def 
def sapa(nama):
    print(nama)
sapa("rifqi")
sapa("haifah")

# pertambahan
def tambah(a,b):
    hasil = a + b
    return hasil
print(tambah(7, 8))

def nilai(a):
    if a % 2 == 0:
        print("genap")
    elif a % 2 == 1:
        print("ganjil")

nilai(74)

# pertambahan
def angka(a,b):
    hasil = a + b
    return(hasil)
angka(3,4)