# Pernyataan If
# 
# Pernyataan if digunakan untuk menjalankan kode hanya jika kondisi tertentu
# bernilai True.
# Setelah if, harus ada : (titik dua)
# Kode yang akan dijalankan jika kondisi True harus diindentasi (diberi spasi di
# awal)

# angka = int(input("Masukkan angka: "))

# if angka > 0:
#     print("Angka yang dimasukkan adalah bilangan positif.")

# if angka < 0:
#     print("Angka yang dimasukkan adalah bilangan negatif.")

# if angka == 0:
#     print("Angka yang dimasukkan adalah nol.")

nilai = int(input("Masukkan angka: "))
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
else:
    print("Nilai Anda C")