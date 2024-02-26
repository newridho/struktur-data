#Buatlah aplikasi sederhana yang memiliki 4 menu: yaitu 1) tambah barang ke keranjang, 2) lihat keranjang, 3) hapus barang dari keranjang, dan 4) keluar program. Aplikasi akan melakukan looping hingga user memilih menu 4. Gunakan list sebagai tempat penampung sementara untuk aplikasi sederhana ini.

def tambah_data(barang):
    barang_baru = input("Masukkan Barang Baru: ")
    barang.append(barang_baru)

    print(f"Barang {barang_baru} berhasil ditambahkan ke keranjang")

def tampil_data(barang):
    if not barang:
        print("Keranjang kosong")
    else:
        print(barang)

def hapus_semuaBarang(barang):
    barang.clear()


def main_menu(barang):
    while True:
        print("\nMenu")
        print("1. Tambah Data ke keranjang")
        print("2. Lihat Barang")
        print("3. Hapus semua barang")
        print("4. Keluar menu")

        menu = input("Pilih Menu: ")
        if menu == '1':
            tambah_data(barang)
        elif menu == '2':
            tampil_data(barang)
        elif menu == '3':
            hapus_semuaBarang(barang)
        elif menu == '4':
            print("Terima Kasih")
            exit()
        else:
            print("Menu Tidak Ada")

if __name__ == "__main__":
    barang = ['barang1', 'barang2', 'barang3']
    main_menu(barang)

    menu = input("Pilih Menu: ")
    if menu == '1':
        tambah_data(barang)
    elif menu == '2':
        tampil_data(barang)
    elif menu == '3':
        hapus_semuaBarang(barang)
    elif menu == '4':
        print("Terima Kasih")
    else:
        print("Menu Tidak Ada")

if __name__ == "__main__":
    main_menu()
