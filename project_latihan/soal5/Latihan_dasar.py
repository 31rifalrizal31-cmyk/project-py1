data_buku = []
def tambah_buku():
    print("\n=== Tambah buku ===")
    id_buku = input("masukkan id buku:")
    nama_buku = input("masukkan nama buku:")
    penulis = input("masukkan nama penulis:")
    stock = input("masukkan stock buku:")
    
    if not id_buku.isdigit():
        print("ID harus angka")
        return
    if not stock.isdigit():
        print("stock harus angka")
        return
    for buku in data_buku:
        if buku["id"] == int(id_buku):
            print("ID buku sudah ada")
            return
    buku_baru = {
        "id" : int(id_buku),
        "judul" : nama_buku,
        "penulis" : penulis,
        "stock" : int(stock)
    }
    data_buku.append(buku_baru)
    print("buku berhasil di tambahkan")
def tampilkan_buku():
    if not data_buku:
        print("buku belum di tambahkan")
        return
    print("\n===DAFTAR BUKU===")

    for buku in data_buku:
        print("ID:", buku["id"])
        print("Judul:", buku["judul"])
        print("penulis:", buku["penulis"])
        print("stock:", buku["stock"])
        print("_________________")
def update_buku():
    print("\n===UPDATE BUKU===")
    id_buku = input("masukkan id buku yang akan di cari:")
    if not id_buku.isdigit():
        print("id harus angka")
        return
    id_buku = int(id_buku)
    
    buku = cari_buku_by_id(int(id_buku))

    if buku is None:
        print("buku tidak di temukan")
judul_baru = input(f"Masukkan judul baru ({buku['judul']}): ")
                  
