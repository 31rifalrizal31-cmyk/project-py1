password = input("daftar kan passwordnya:")
verifikasi = input("masukkan passwordnya:")
while verifikasi != password:
    print("password salah")
    verifikasi = input("masukkan lagi pw nya:")
    if verifikasi == password:
        print("password benar")
