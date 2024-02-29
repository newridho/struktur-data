class Karyawan:
    def __init__(self,nama,usia):
        self.nama = nama
        self.usia = usia

    data = {
        "Ridhoo": {"usia":22, "alamat": "gaji"}
    }

    def tampil_data(self):
        print("Nama: ", self.nama)
        print("Usia: ", self.usia)

    def set_nama(self, nama):
        self.nama = nama
    
    def set_usia(self, usia):
        self.usia = usia

def main():
    kar = Karyawan("Fathur", 23)
    kar.set_nama("Agus")
    kar.tampil_data()
    
if __name__ == "__main__":
    main()