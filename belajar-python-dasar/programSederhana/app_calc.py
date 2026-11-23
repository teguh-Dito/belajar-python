def app_penjumlahan():
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 + angka2
    print("hasil penjumlahan", hasil)
    print("=== program penjumlahan selesai ====")

def app_pengurangan():
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 - angka2
    print("hasil pengurangan", hasil)
    print("=== program pengurangan selesai ====")

def app_perkalian():
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 * angka2
    print("hasil perkalian", hasil)
    print("=== program perkalian selesai ====")

def app_pembagian():
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 / angka2
    print("hasil pembagian", hasil)
    print("=== program pembagian selesai ====")

def app_menu():
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("x. keluar")
        print("=== PROGRAM KALKULATOR SEDERHANA ===")

        pilihan = int(input("pilihan: "))

        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("=== SAMPAI JUMPA LAGI ===")
            break

app_menu()

# Tambahkan try-except agar program tidak crash ketika terjadi error