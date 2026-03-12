angka = int(input("masukkan angkanya:"))
if angka > 0: 
    print("angka yang kamu masukkan masuk ke dalam bilangan positif")
elif angka == 0: 
    print("angkau yang kamu masukan adalah nol")
else:
    print("angka yang kamu masukkan masuk ke dalam bilangan negatif")
nilai = int(input("masukkan nilai kamu:"))
if nilai >= 90:
    print("nilai kamu di atas rata rata")
else:
    print("nilai kamu di bawah rata rata")
password = input("masukkan password kamu:") 
if password == "12345":
    print("password kamu benar")
else:
    print("password kamu salah")
angka_pertama = int(input("masukkan angka pertama:"))
angka_kedua = int(input("masukkan angka ke dua:"))
angka_ketiga = int(input("masukkan angka ketiga:"))
if angka_pertama > angka_kedua and angka_pertama > angka_ketiga:
    print("angka pertama adalah angka terbesar")
elif angka_kedua > angka_pertama and angka_kedua > angka_ketiga:
    print("angka kedua adalah angka terbesar")
else:
    print("angka ketiga adalah angka terbesar")