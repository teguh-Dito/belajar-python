nama = "Budi"
umur = 25

# pesan = "Nama saya  " + nama + " dan umur saya " + umur + " tahun."
pesan = "Nama saya  " + nama + " dan umur saya " + str(umur) + " tahun."
print(pesan)

print(len(nama))
print(len(str(umur)))

print("PENGGUNAAN INDEX PADA STRING")
print("Ini adalah nama ")
nama = "Python"
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])
print(nama[4])
print(nama[5])

print("Ini adalah nama negative index")
print(nama[-1])
print(nama[-2])
print(nama[-3])
print(nama[-4])
print(nama[-5])
print(nama[-6])

print("PENGGUNAAN SLICING PADA STRING")
print(nama[0:3])
print(nama[2:5])
print(nama[:3])
print(nama[2:])
print(nama[:])


# METHODS
# UPPER, LOWER, TITLE, CAPITALIZE, REPLACE, SPLIT, REPLACE, COUNT, FIND, JOIN, STRIP
nama = "Alice"
print(nama)
nama_upper = nama.upper()
print(nama_upper)
nama_lower = nama.lower()
print(nama_lower)
nama_title = nama.title()
print(nama_title)
nama_capitalize = nama.capitalize()
print(nama_capitalize)

nama = "  Teguh  "
nama_strip = nama.strip()
print(nama_strip)

kalimat = "I Love C++"
kalimat_baru = kalimat.replace("C++", "Python")
print(kalimat_baru)

nama = "teguh darma pinandhita"
jumlah_a = nama.count("a")
print(jumlah_a)

kalimat = "Python adalah bahasa pemrograman yang menyenangkan"
posisi = kalimat.find("bahasa")
print(posisi)

# Escape Character
# \n = new line, \t = tab, \\ = backslash, \' = single quote, \" = double quote
print("ESCAPE CHARACTER")
print("Ini adalah baris pertama\nIni adalah baris kedua")

kalimat = "Nama:\tTeguh\nUmur:\t25\nAlamat:\tJakarta"
print(kalimat)

path = "C:\\Users\\Teguh\\Documents\\BelajarPython"
print(path)


# STRING INTERPOLATION
nama = "Teguh"
umur = 25

# menggunakan f-string
profil = f"Nama saya {nama} dan umur saya {umur} tahun."
print(profil)

# lebih jelas dari concatenation, lebih mudah dibaca, dan lebih efisien
profil_lama = "Nama saya " + nama + " dan umur saya " + str(umur) + " tahun."
print(profil_lama)

harga = 100000
jumlah = 3

# Operasi matematika dalam f-string
total = f"Total harga: {harga * jumlah}"
print(total)

# Method Cells dalam f-string
nama = "teguh darma pinandhita"
salam = f"Nama saya {nama.upper()}"
print(salam)
