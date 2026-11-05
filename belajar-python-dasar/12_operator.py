print("OPERATOR ARITMATIKA")
a = 10 
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a % b)

print(10 % 2)
print(11 % 2)

a = 2
b = 3
print(a ** b)
print(5 ** 2)
print(3 ** 4)


# ASSIGNMENT (OPERATOR ASSIGNMENT & COMPOUND ASSIGNMENT)
print("\nASSIGNMENT (OPERATOR ASSIGNMENT & COMPOUND ASSIGNMENT)")
x = 10
print("x awal:", x)

x += 5
print("x setelah ditambah 5:", x)

x -= 3
print("x setelah dikurangi 3:", x)

x *= 2
print("x setelah dikali 2:", x)

x /= 4
print("x setelah dibagi 4:", x)

#  OPERATOR PERBANDINGAN
print("\nOPERATOR PERBANDINGAN")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

nama1 = "Teguh"
nama2 = "Darma"
nama3 = "Teguh"

print(nama1 == nama2)
print(nama1 == nama3)
print(nama1 != nama2)

# OPERATOR LOGIKA
print("\nOPERATOR LOGIKA")
umur = 25
print(umur > 18 and umur < 30)

hari = "Senin"
print(hari == "Senin" or hari == "Selasa")

aktif = True
print(not aktif)


#  OPERATOR STRING
nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

kata = "Hello"
print(kata * 3)

garis = "-"
print(garis * 10)

kalimat = "Python is awesome"
print("Python" in kalimat)
print("Java" in kalimat)
print("is" in kalimat)
print ("is" not in kalimat)


# Prioritas Operator
# Operator memiliki urutan prioritas (precedence). Operator dengan prioritas lebih tinggi akan dieksekusi terlebih dahulu
# Urutan Prioritas (dari tinggi ke rendah):
# 
# ** (pangkat)
# * , l, //, % (perkalian, pembagian)
# +, - (penjumlahan, pengurangan)
# <=, >= (perbandingan)
# not (logika not)
# and (logika and)
# or (logika or)