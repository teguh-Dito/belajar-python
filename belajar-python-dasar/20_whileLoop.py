# Mencetak angka 1 sampai 5 
angka = 1
while angka <= 5:
    print(angka)
    angka += 1

# Input sampai benar 
password = ''
while password != "12345678":
    password = input("Masukkan password anda: ")
    if password != "12345678":
        print("Password Salah!, coba lagi!")
print("Password benar!")