# Game Tebak Angka Dengan Break
# Penggunaan Break
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak Angka (1-10): "))
    if tebakan == angka_rahasia:
        print("Selamat! anda benar")
        break
    else:
        print("Salah, Coba lagi!")


# Mencetak angka ganjil saja
# Penggunaan Continue
for i in range(10):
    if i % 2 == 0:
        continue 
    print(i)