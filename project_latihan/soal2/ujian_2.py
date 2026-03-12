nama = input("masukkan nama kamu:")
umur = int(input("masukkan umur kamu:"))
print("namamu adalah", nama, "umurmu juga adalah", umur, "tahun, dan di sepuluh tahun ke depan umur mu adalah", umur + 10, "tahun")

nilai = int(input("masukkan nilai kamu:"))
if nilai >= 90:
    print("nilai yang sangat besar")
elif nilai >= 70:
    print("lumayan")
elif nilai >= 50:
    print("buruk")
else:
    print("mana angkana woy")
    
#ganjil dan genap
angka = int(input("masukkan angkanya:"))
if angka % 2 == 0:
    print("genap")
else:
    print("ganjil")

# login sederhana
username = input("masukkan username kamu:")
password = int(input("masukkan password kamu:"))
if username == "rifqi" and password == 123456:
    print("anda telah login")
elif username != "rifqi" and password == 123456:
    print("username anda salah")
elif username == "rifqi" and password != 123456:
    print("password anda salah")
    
#klasifikasi umur
umur = int(input("masukkan umur kamu"))
if umur >= 30:
    print("kamu sudah dewasa")
elif umur >= 20:
    print("kamu masih remaja")
elif umur >= 10:
    print("kamu masih kecil")
elif umur >= 0:
    print("kamu masih bayi")

#meminta angka
a = int(input("masukkan angka pertama"))
b = int(input("masukkan angka kedua"))
c = int(input("masukkan angka ketiga"))

if a > b and a > c and b > c:
    print(a, b, c )
elif b > a and b > c and a > c:
    print(b, a, c )
elif c > a and c > b and b > a:
    print( c, b, a)
# dan seterus nya

a = int(input("masukkan angka pertama"))
b =  int(input("masukkan angka kesua"))
c = input("operator (+, -, *, /):")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - c)
elif c == "*":
    print(a * c)
elif c == "/":
    print(a / b)
else:
    print("angka tidak valid")


    print("eweh suaraan")