# List Kosong
daftar_kosong = []

# List dengan angka 
angka = [1,2,3,4,5]
print(angka)

# List dengan string 
nama = ["Alice", "Bob", "Charlie"]
print(nama)

# List Campuran 
Campuran = ["Alice", 25, "Bob", 30]
print(Campuran)

# Mengakses elemen
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

# Mengubah elemen 
warna = ["merah", "biru", "kuning"]
print(warna)

warna[2] = "Orange"
print(warna)

buah = ["apel", "jeruk"]
print(buah)

buah.append("durian")
print(buah)

buah.insert(1, "Mangga")
print(buah)

buah.remove("jeruk")
print(buah)

del buah[0]
print(buah)

print(len(buah))

satu = [1,2,3]
print(satu)
dua = [4,5,6]
print(dua)

mix = satu + dua
print(mix)

print("=== LOOPING ===")
banyak_buah = ["apel", "jeruk", "durian", "mangga"]
for buah in banyak_buah:
    print("\n" + buah + "\n")

    for i in range(0, len(banyak_buah)):
        print(banyak_buah[i])

    if "durian" in banyak_buah:
        print("ada durian")
    else:
        print("Tidak ada durian")