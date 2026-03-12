umur = int(input("masukkan umur anda:"))
if umur < 18:
    print("kamu samih remaja")
else:
    print("kamu sudah dewasa")

i = 1
for i in range(10):
    print(i + 1)

def kali(a, b):
    hasil = a * b
    return hasil
print(kali(3, 5))

buah = ["apel", "mangga", "pisang"]
buah.append("jeruk")
buah.remove("mangga")
print(buah)

angka = [2, 4, 6, 8]
for i in angka:
    print(i * 2)

angka = []
for i in range(3):
    nomor = int(input("masukkan angkanya:"))
    angka.append(nomor)
print(angka)

angka = []
for i in range(3):
    nomor = int(input("masukkan angkanya:"))
    angka.append(nomor)
print(sum(angka))

