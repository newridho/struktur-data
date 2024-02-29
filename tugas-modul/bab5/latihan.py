#Buatlah class dengan nama kalkulator yang mempunyai 2 parameter yaitu angka 1 dan angka 2. Kemudian tambahkan metode ini pada kelas tersebut:
# 1. setBilangan1 : yang akan mengubah nilai bilangan 1
# 2. setBilangan2 : yang akan mengubah nilai bilangan 2
# 3. tambah() : yang akan menampilkan hasil penjumlahan antara bilangan 1 dan 2
# 4. Pangkat() : yang akan menampilkan hasil bilangan1 pangkat bilangan 2

class Calculator:
    def __init__(self, bilangan1, bilangan2):
        self.bilangan1 = bilangan1
        self.bilangan2 = bilangan2

    def setbilangan1(self, bilangan1):
        self.bilangan1 = bilangan1

    def setbilangan2(self, bilangan2):
        self.bilangan2 = bilangan2

    def tambah(self):
        return self.bilangan1 + self.bilangan2

    def pangkat(self):
        result = 1
        for _ in range(self.bilangan2):
            result *= self.bilangan1
        return result

if __name__ == "__main__":
    while True:
        print("1. Tambah")
        print("2. Pangkat")
        print("3. Keluar")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            bil1 = int(input("Masukkan angka ke-1: "))
            bil2 = int(input("Masukkan angka ke-2: "))
            calc = Calculator(bil1, bil2)
            print("Hasil: ", calc.tambah())
        elif choice == "2":
            bil1 = int(input("Masukkan angka: "))
            bil2 = int(input("Masukkan eksponennya (pangkat): "))
            calc = Calculator(bil1, bil2)
            print("Hasil: ", calc.pangkat())
        elif choice == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan salah!")
