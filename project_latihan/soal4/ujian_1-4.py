nama = input("masukkan nama kamu:")
umur = int(input("masukkan juga umur kamu:"))
print(f'nama kamu adalah {nama}, juga umur kamu sekarang adalah {umur}, dan di 10 tahun ke dapan umur kamu adalah {umur + 10}')
#cek angka 
def cek_angka(angka):
    if angka % 2 == 0:
        print("genap")
    else:
        print("ganjil")
cek_angka(20)
# meminta nilai
def nilai(angka):
    if angka >= 90:
        print("A")
    elif angka >= 80:
        print("B")
    elif angka >= 70:
        print("C")
    elif angka >= 60:
        print("D")
    else:
        print("nilai kamu buruk sekali")
nilai(60)
# penjumlahan beruntun
total = 0
for i in range(5):
    angka = int(input("masukkan angkanya:"))
    total += angka
    print(total)
#while password
password = "python123"
verifikasi = input("masukkan password nya:")
while verifikasi != password:
    print("kata sandi salah")
    verifikasi = input("masukkan lagi kata sandinya:")
print("anda telah login")
#bagian bintang
for i in range(5):
    for j in range(4):
        print("*", end="")
    print()
#kalkulator sederhana
a = int(input("masukkan angka pertama:"))
b = int(input("masukkan angka kedua:"))
print(a + b, "jika di tambah")
print(a - b, "jika di kurangi")
print(a / b, "jika dibagi")
print(a * b, "jika di kali")

i = 1


while True:
    kata = input("masukkan katanya:")
    if kata == "exit":
        break
    print("kamu berkata", kata)
print("kamu menyuruh berhenti")

def sisi(a):
    b = a
    hasil = a * b
    return hasil
sisi(3)
