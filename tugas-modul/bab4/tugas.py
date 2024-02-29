#Buatlah dictionary yang berisi daftar seluruh pemain pada tim olahraga favorit Anda (sepak bola, basket, voli) dengan catatan olahraga tersebut menggunakan nomor punggung pemain yang unik. Jadikan nomor punggung sebagai key dan nama lengkap sebagai value pada dictionary Anda. Setelah berhasil dibuat, tampilkan seluruh nama dan nomor punggung pemain di dalam dictionary.
pemain_basket = {
    6: "Seseorang1",
    8: "Seseorang2",
    26: "Seseorang3",
    28: "Seseorang4",
    16: "Seseorang5"
}

for tim1, nama in pemain_basket.items():
    print(f"Nomor Jersey: {tim1}, Nama Pemain: {nama}")