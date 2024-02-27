#Buatlah class dengan nama kalkulator yang mempunyai 2 parameter yaitu angka 1 dan angka 2. Kemudian tambahkan metode ini pada kelas tersebut:
# 1. setNumber1 : yang akan mengubah nilai bilangan 1
# 2. setNumber2 : yang akan mengubah nilai bilangan 2
# 3. add() : yang akan menampilkan hasil penjumlahan antara bilangan 1 dan 2
# 4. Pangkat() : yang akan menampilkan hasil bilangan1 pangkat bilangan 2

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def setNumber1(self, number1):
        self.number1 = number1

    def setNumber2(self, number2):
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def power(self):
        result = 1
        for _ in range(self.number2):
            result *= self.number1
        return result

if __name__ == "__main__":
    while True:
        print("1. Tambah")
        print("2. Pangkat")
        print("3. Exit")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            num1 = int(input("Masukkan angka ke-1: "))
            num2 = int(input("Masukkan angka ke-2: "))
            calc = Calculator(num1, num2)
            print("Hasil: ", calc.add())
        elif choice == "2":
            num1 = int(input("Masukkan angka: "))
            num2 = int(input("Masukkan eksponennya (pangkat): "))
            calc = Calculator(num1, num2)
            print("Hasil: ", calc.power())
        elif choice == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan salah!")
