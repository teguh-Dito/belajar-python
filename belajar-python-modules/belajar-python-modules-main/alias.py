import matematika as math

def tambah(a, b):
    print("Fungsi tambah")
    return a + b

if __name__ == "__main__":

    hasil1 = math.tambah(10, 5)
    hasil2 = math.kali(7, 3)

    print(f"Hasil dari 10 + 5 = {hasil1}")
    print(f"Hasil dari 7 * 3 = {hasil2}")

    print(f"Nilai PI : {math.PI}")
    print(f"Pembuat : {math.NAMA_PEMBUAT}")