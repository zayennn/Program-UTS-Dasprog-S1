nama_produk = [
    "Bakso Mercon",
    "Roti Stuff",
    "Mocktail"
]

harga_produk = [
    10000,
    5000,
    5000
]

while True :
    print("""
======================= 3VOURS =======================

# PILIH ROLE KAMU :
1) PENJUAL
2) PEMBELI
""")
    
    userRole = int(input('input role kamu (1/2) : '))


    if userRole == 1:
        while True:
            print("\n===== LIST BARANG 3VOURS =====")
            for i in range(len(nama_produk)):
                print(f"{i+1}. {nama_produk[i]} - Rp{harga_produk[i]}")

            print("\nAksi : ")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("0. Kembali ke menu awal")

            userAction = input("Pilih aksi (1/2/0): ")

            if userAction == "1":
                nama_add = input("Nama barang: ")
                harga_add = int(input("Harga: "))
                nama_produk.append(nama_add)
                harga_produk.append(harga_add)
                print("\nBarang berhasil ditambahkan!")

            elif userAction == "2":
                hapus = int(input("Nomor barang yang ingin dihapus: "))
                if 1 <= hapus <= len(nama_produk):
                    nama_produk.pop(hapus-1)
                    harga_produk.pop(hapus-1)
                    print("\nBarang berhasil dihapus!")
                else:
                    print("Nomor barang tidak valid!")

            elif userAction == "0":
                print("\nKembali ke menu utama...\n")
                break

            else:
                print("Aksi tidak valid!")

    
    elif userRole == 2:
        print("\n======================= Daftar Produk 3Vours =======================\n")
        for i, (nama, harga) in enumerate(zip(nama_produk, harga_produk), start=1):
            print(f"{i}. {nama} = Rp {harga}")

        jumlah_jenis = int(input('\nMasukkan jumlah jenis produk yang ingin dibeli : '))

        total_belanja = 0
        pesanan = []

        for i in range(1, jumlah_jenis + 1):
            print(f"\nJenis ke-{i}")

            pilih_produk = int(input('Pilih produk: '))
            jumlah_beli = int(input('Jumlah produk : '))

            if 1 <= pilih_produk <= len(nama_produk):
                nama_barang = nama_produk[pilih_produk - 1]
                harga_satuan = harga_produk[pilih_produk - 1]

                total_harga = harga_satuan * jumlah_beli

                pesanan.append([nama_barang, jumlah_beli, total_harga])
                total_belanja += total_harga

                print(f"{nama_barang} x {jumlah_beli} = Rp {total_harga}")
            else:
                print("Produk tidak ditemukan")

        print("\n======================= TOTAL BELANJA =======================")
        for item in pesanan:
            print(f"{item[0]} x {item[1]} = Rp {item[2]}")

        if total_belanja > 100000:
            diskon = total_belanja * 0.1
            total_belanja -= diskon
            print("\nDiskon 10% aktif!")

        print(f"\nTOTAL YANG HARUS DIBAYAR = Rp {total_belanja}\n")

    else:
        print('Pilihan tidak valid!')
