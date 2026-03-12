data_buku = []

def tampilkan_buku():
    if not data_buku:
        print("\nData buku masih kosong.")
        return

    print("\nDaftar Buku:")
    for buku in data_buku:
        print(f"ID: {buku['id']} | Judul: {buku['judul']} | Penulis: {buku['penulis']} | Stok: {buku['stok']}")

def tambah_buku():
    print("\n=== Tambah Buku ===")
    id_buku = input("Masukkan ID: ")
    judul = input("Masukkan judul: ")
    penulis = input("Masukkan penulis: ")
    stok = input("Masukkan stok: ")

    if not id_buku.isdigit():
        print("ID harus angka.")
        return

    if not stok.isdigit():
        print(" harus angka.")
        return

    for buku in data_buku:
        if buku["id"] == int(id_buku):
            print("ID sudah ada.")
            return

    buku_baru = {
        "id": int(id_buku),
        "judul": judul,
        "penulis": penulis,
        "stok": int(stok)
    }

    data_buku.append(buku_baru)
    print("Buku berhasil ditambahkan.")

def cari_buku_by_id(id_buku):
    for buku in data_buku:
        if buku["id"] == id_buku:
            return buku
    return None

def update_buku():
    print("\n=== Update Buku ===")
    id_buku = input("Masukkan ID buku yang ingin diupdate: ")

    if not id_buku.isdigit():
        print("ID harus angka.")
        return

    buku = cari_buku_by_id(int(id_buku))

    if buku is None:
        print("Buku tidak ditemukan.")
        return

    judul_baru = input(f"Judul baru ({buku['judul']}): ")
    penulis_baru = input(f"Penulis baru ({buku['penulis']}): ")
    stok_baru = input(f"Stok baru ({buku['stok']}): ")_

    if judul_baru:
        buku["judul"] = judul_baru
    if penulis_baru:
        buku["penulis"] = penulis_baru
    if stok_baru:
        if stok_baru.isdigit():
            buku["stok"] = int(stok_baru)
        else:
            print("Stok harus angka.")
            return

    print("Data buku berhasil diupdate.")

def hapus_buku():
    print("\n=== Hapus Buku ===")
    id_buku = input("Masukkan ID buku yang ingin dihapus: ")

    if not id_buku.isdigit():
        print("ID harus angka.")
        return

    buku = cari_buku_by_id(int(id_buku))

    if buku is None:
        print("Buku tidak ditemukan.")
        return

    data_buku.remove(buku)
    print("Buku berhasil dihapus.")

def cari_buku():
    print("\n=== Cari Buku ===")
    keyword = input("Masukkan judul buku: ").lower()

    hasil = []
    for buku in data_buku:
        if keyword in buku["judul"].lower():
            hasil.append(buku)

    if not hasil:
        print("Buku tidak ditemukan.")
        return

    print("\nHasil Pencarian:")
    for buku in hasil:
        print(f"ID: {buku['id']} | Judul: {buku['judul']} | Penulis: {buku['penulis']} | Stok: {buku['stok']}")

def menu():
    while True:
        print("\n=== MENU MANAJEMEN BUKU ===")
        print("1. Tambah buku")
        print("2. Lihat semua buku")
        print("3. Update buku")
        print("4. Hapus buku")
        print("5. Cari buku")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_buku()
        elif pilihan == "3":
            update_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            cari_buku()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menu()