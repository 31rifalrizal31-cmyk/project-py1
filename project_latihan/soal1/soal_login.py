username = input("masukkan username kamu:")
password = int(input("masukkan password kamu:"))
if username == "rifqi" and password == 12345:
    print("login berhasil")
elif username == "rifqi"and password != 12345:
    print("password kamu salah")
elif username != "rifqi" and password == 12345:
    print("username kamu salah")
else:
    print("username dan password kamu salah")