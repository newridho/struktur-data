#Buatlah dictionary yang berisi daftar seluruh pemain pada tim olahraga favorit Anda (sepak bola, basket, voli) dengan catatan olahraga tersebut menggunakan nomor punggung pemain yang unik. Jadikan nomor punggung sebagai key dan nama lengkap sebagai value pada dictionary Anda. Setelah berhasil dibuat, tampilkan seluruh nama dan nomor punggung pemain di dalam dictionary.
pemain_basket = {
    6: "Wahyu",
    8: "Joko",
    26: "Juni",
    28: "Hantoro",
    16: "Seseorang"
}

for tim1, nama in pemain_basket.items():
    print(f"Nomor Jersey: {tim1}, Nama Pemain: {nama}")