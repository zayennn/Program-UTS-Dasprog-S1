productLists = [
    "Bakso Mercon",
    "Roti Stuff",
    "Mocktail"
]

productPrices = [
    10000,
    5000,
    5000
]

while True :
    print("""
======================= DAFTAR MENU 3 VOURS =======================

# PILIH ROLE KAMU :
1) PENJUAL
2) PEMBELI
""")
    
    userRole = int(input('input role kamu (1/2) : '))

    if userRole == 1:
        print("\n======================= List Menu Makanan 3 Vours =======================\n")
        for i, (name, price) in enumerate(zip(productLists, productPrices), start=1):
            print(f"{i}) {name} : Rp {price}")
            
        print(f"""
=======================  Pilih Aksi Kamu =======================
1) Tambah Product
2) Hapus Barang
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
            
    elif userRole == 2 :
        print("\n======================= List Products 3Vours =======================\n")
        for i, (name, price) in enumerate(zip(productLists, productPrices), start=1) :
            print(f"{i}. {name} = {price}")
            
        jum_jenis = int(input('\nmasukan jumlah product yang ingin kamu beli : '))
        
        for i in range(1, jum_jenis + 1) :
            print(f"\njenis ke-{i}")
            
            i_product = int(input('pilih jenis barang (1/2/3) : '))
            jum_beli = int(input('jumlah product : '))

            if i_product == 1 :
                total = productPrices[0] * jum_beli
                print(f"{productLists[0]} x {jum_beli} = {total}\n")
            elif i_product == 2 :
                total = productPrices[1] * jum_beli
                print(f"{productLists[1]} x {jum_beli} = {productPrices[1] * jum_beli}")
            elif i_product == 3 :
                total = productPrices[2] * jum_beli
                print(f"{productLists[2]} x {jum_beli} = {productPrices[2] * jum_beli}")
            else :
                print("product tidak ditemukan")
                
            print(f"total yang harus dibayar : {total}")

    else :
        print('pilihan kamu tidak valid')