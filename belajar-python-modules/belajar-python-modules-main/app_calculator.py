from calculator import operasi

if __name__ == "__main__":
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("=== PROGRAM KALKULATOR SEDERHANA ===")

        try:
            pilihan = int(input("Pilihan: "))

            if pilihan == 1:
                operasi.app_penjumlahan()
            elif pilihan == 2:
                operasi.app_pengurangan()
            elif pilihan == 3:
                operasi.app_perkalian()
            elif pilihan == 4:
                operasi.app_pembagian()
            elif pilihan == 5:
                print("=== SAMPAI JUMPA LAGI ===")
                break
            else:
                print("Error: Pilihan tidak valid")
        except ValueError:
            print("Error: Masukkan nomor pilihan yang valid")

# tambahkan try-except agar program tidak crash ketika terjadi error