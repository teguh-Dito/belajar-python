import random

def tebak_angka():
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan:
        tebakan += 1
        try:
            angka_user = int(input("Masukkan angka: "))
            if angka_user > angka_acak:
                print("Angka terlalu besar")
            elif angka_user < angka_acak:
                print("Angka terlalu kecil")
            else:
                print("Selamat, Angka benar")
                break
        except ValueError:
            print("Error: Masukkan angka yang valid")
            tebakan -= 1
    else:
        print("Kamu telah melewati maksimal tebakan anda")
        print("Angka acak adalah", angka_acak)

    input("Enter untuk lanjut")