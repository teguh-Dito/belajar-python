# Ternary Operator / Conditional Expression

angka = int(input("Masukkan angka: "))

# Dengan if-else biasa
# if angka > 0 
#     hasil = "Angka positif"
# else:
#     hasil = "Angka negatif atau nol"

# Dengan conditional expression
hasil = "Angka positif" if angka > 0 else "Angka negatif atau nol"
print("Angka tersebut: ", hasil)