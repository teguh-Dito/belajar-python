# Buat angka random
# Hint "Terlalu besar" atau "terlalu kecil"
# Hitung jumlah tebakan
# angka maksimal tebakan


def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    tebakan = 0
    max_tebakan = 3
    while tebakan < max_tebakan:
        tebakan += 1
        angka_user = int(input("Masukkan angka: "))
        if angka_user > angka_acak:
            print("Angka terlalu besar")
        elif angka_user < angka_acak:
            print("Angka terlalu kecil")
        else:
            print("Selamat, angka anda benar")
            break
    else:
        print("Kamu telah melewati maksimal tebakan anda")
        print("Angka acak adalah", angka_acak)
    
    input("Enter untuk lanjut")
    
def app_menu():
    while True:
        print("===  PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("===  PROGRAM TEBAK ANGKA SEDERHANA ===")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("=== Program tebak angka selesai ===")
            break
        else:
            print("Error: pilihan tidak valid!")

app_menu()