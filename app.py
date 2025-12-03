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
======================= DAFTAR MENU 3VOURS =======================

# PILIH ROLE KAMU :
1) PENJUAL
2) PEMBELI
""")
    
    userRole = int(input('input role kamu (1/2) : '))

    if userRole == 1:
        print("\n======================= List Menu Makanan 3Vours =======================\n")
        for i, (nama, harga) in enumerate(zip(nama_produk, harga_produk), start=1):
            print(f"{i}) {nama} : Rp {harga}")
        
        print("""
=======================  Pilih Aksi Kamu =======================
1) Tambah Produk
2) Hapus Produk
3) Keluar
""")
        
        userAction = int(input('masukan aksi kamu (1/2/3) : '))

        if userAction == 1 :
            pass
        elif userAction == 2 :
            pass
        elif userAction == 3 :
            break
        else :
            print('pilihan kamu tidak valid!')
    
    elif userRole == 2:
        print("\n======================= Daftar Produk 3Vours =======================\n")
        for i, (nama, harga) in enumerate(zip(nama_produk, harga_produk), start=1):
            print(f"{i}. {nama} = Rp {harga}")

        jumlah_jenis = int(input('\nMasukkan jumlah jenis produk yang ingin dibeli : '))

        total_belanja = 0
        pesanan = []

        for i in range(1, jumlah_jenis + 1):
            print(f"\nJenis ke-{i}")

            pilih_produk = int(input('Pilih produk (1/2/3): '))
            jumlah_beli = int(input('Jumlah produk : '))

            if 1 <= pilih_produk <= len(nama_produk):
                nama_produk = nama_produk[pilih_produk - 1]
                harga_satuan = harga_produk[pilih_produk - 1]
                total_harga = harga_satuan * jumlah_beli

                pesanan.append([nama_produk, jumlah_beli, total_harga])
                total_belanja += total_harga

                print(f"{nama_produk} x {jumlah_beli} = Rp {total_harga}")
            else:
                print("Produk tidak ditemukan")

        print("\n======================= TOTAL BELANJA =======================")
        for item in pesanan:
            print(f"{item[0]} x {item[1]} = Rp {item[2]}")

        print(f"\nTOTAL YANG HARUS DIBAYAR = Rp {total_belanja}\n")

    else:
        print('Pilihan tidak valid!')