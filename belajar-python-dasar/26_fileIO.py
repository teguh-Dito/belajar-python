## Apa itu File 1/0 (Input/0utput)?
# File 1/0 (Input/Output) adalah kemampuan program untuk membaca data dari
# file dan menulis data ke file.
# Dengan file 1/0, kita bisa:
# Menyimpan data secara permanen
# Membaca data yang sudah tersimpan
# Membuat laporan dalam bentuk file
# Memproses data dari file eksternal
# Backup dan restore data aplikasi

## Membuka dan Menutup File
# Untuk membuka file, kita bisa menggunakan function open(file, mode)
# Setelah selesai membuka file, jangan lupa tutup menggunakan function close()
# pada variabelnya
# Saat membuka file, kita harus tentukan mode nya

## Mode File
# |---------------------------------------------------------------------------------------|
# | Mode      | Deskripsi             | Contoh Penggunaan                                 |
# | r         | Read (baca)           | Membaca file yang sudah ada                       |
# | w         | Write (tulis)         | Menulis file baru atau menimpa file lama          |
# | a         | Append (tambah)       | Menambah data di akhir file                       |
# | x         | Create (buat)         | Membuat file baru, error jika sudah ada           |
# |---------------------------------------------------------------------------------------|

print("\n############ MENULIS KE FILE ############")
print("=== SIMPAN DATA NILAI ===")

file = open("simpan_nilai.txt", "w")

while True:
    nama = input("Nama siswa (enter untuk selesai): ")
    if nama == "":
        break
    
    nilai = input("Nilai: ")

    # Tulis ke file
    file.write(nama + "," + nilai + "\n")
    print("Data", nama, "Berhasil disimpan")

file.close()
print("Semua data berhasil disimpan ke nilai_siswa.txt")

print("\n############ MENAMPILKAN DATA FILE ############")
with open("simpan_nilai.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        print(data[0], ":", data[1])

print("=== DATA SELESAI ===")