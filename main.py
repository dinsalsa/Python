list_buku = []

while True:
    print("="*10, "Data Buku", "="*10)
    Judul = input("Masukkan Judul Buku \t= ")
    Penulis = input("Masukkan Penulis Buku \t= ")
    Peminjam = input("Nama Peminjam \t\t= ")
    
    buku_baru = [Judul, Penulis, Peminjam]
    list_buku.append(buku_baru)

    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} | {buku[2]}")

    selesai = input("Apakah sudah selesai? (y/n) = ")

    if selesai == 'n':
        break 