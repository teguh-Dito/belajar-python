def app_penjumlahan():
    print("=== PROGRAM PENJUMLAHAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 + angka2
        print("hasil penjumlahan", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program penjumlahan selesai ===")
    input("Enter untuk lanjut")

def app_pengurangan():
    print("=== PROGRAM PENGURANGAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 - angka2
        print("hasil pengurangan", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program pengurangan selesai ===")
    input("Enter untuk lanjut")

def app_perkalian():
    print("=== PROGRAM PERKALIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 * angka2
        print("hasil perkalian", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program perkalian selesai ===")
    input("Enter untuk lanjut")

def app_pembagian():
    print("=== PROGRAM PEMBAGIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 / angka2
        print("hasil pembagian", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol")
    print("=== Program pembagian selesai ===")
    input("Enter untuk lanjut")