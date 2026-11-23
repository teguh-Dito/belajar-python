# print("Hello World" <== ERROR 


# CONTOH NAME ERROR
# variabel 'nama' belum di daftarkan 
# print(nama)


# TypeERROR
# Tidak bisa menambah string dengan angka
# print("5" + 5) 

# ValueError
# tidak bisa convert 'abc' ke int
# angka = int("abc")

# IndexError
# list_data [1,2,3]
# index 5 tidak ada
# print(list_data[5])

# KeyError 
# key tidak valid / tidak ditemukan
# data = {"nama": "Alice"}
# key "umur" tidak ada
# print(data["umur"])

# ZeroDivisionError
# tidak bisa dibagi dengan 0
# print(10 / 0)


print("Gunakan try-Except untuk penanganan error yang mungkin terjadi")

print("=== KALKULATOR SEDERHANA ====")
try: 
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))
    hasil = angka1 / angka2
    print("Hasil: ", hasil)
except: 
    print("Terjadi error dalam perhitungan")

print("\n############ PENANGANAN ERROR SPESIFIK ############")
try:
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    hasil = a / b
    print("Hasil pembagian:", hasil)
except ValueError:
    print("Mohon masukkan angka yang valid")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")
except: 
    print("Terjadi kesalahan yang lain!")


print("\n############ PENANGANAN ERROR DENGAN TRY-EXCEPT-ELSE ############")
try: 
    angka = int(input("Masukkan angka: "))
except ValueError: 
    print("Input tidak valid!")
else:
    print("Angka yang Anda masukkan: ", angka)
    if angka > 0:
        print("Angka Positif")
    elif angka < 0 
        print("Angka negatif")
    else:
        print("Angka nol")

print("\n############ PENANGANAN ERROR DENGAN TRY-EXCEPT-FINALLY ############")
try: 
    angka = int(input("Masukkan angka: "))
    print("Angka Anda:", angka)
except ValueError:
    print("Input tidak valid")
finally:
    print("Program selesai dijalankan")