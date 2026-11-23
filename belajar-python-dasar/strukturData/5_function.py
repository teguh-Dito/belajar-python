def nama_func():
    print("Hello dari function")

# Memanggil func
nama_func()
# nama_func()
# nama_func()

## FUNC DENGAN PARAMETER
print("\n############ FUNC DENGAN PARAMETER ############")
def sapa_nama(nama):
    print("Halo", nama)
    print("Senang bertemu dengan anda")

# Memanggil function dengan argument
sapa_nama("Alice")
sapa_nama("Salsa")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang : ", luas)

hitung_luas_persegi_panjang(10, 5)
hitung_luas_persegi_panjang(3, 4)

## FUNC DENGAN RETURN VALUE
print("\n############ FUNC DENGAN RETURN VALUE ############")
def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(10)
luas2 = hitung_luas_lingkaran(21)

print("Luas lingkaran", luas1)
print("Luas lingkaran", luas2)
print("Total Luas: ", luas1 + luas2)


## FUNC DENGAN DEFAULT PARAMETER
print("\n############ FUNC DENGAN DEFAULT PARAMETER ############")
def sapa(nama, sapaan="Halo"):
    print(sapaan, nama)

sapa("Alice")
sapa("Bob", "Hi")
sapa("Charlie", "Hey")

print("\n############ FUNC DENGAN KEYWORD ARGUMENT ############")
def perkenalan(nama, umur, kota):
    print("Nama: ", nama)
    print("Umur: ", umur, " tahun")
    print("Asal: ", kota)
    print("---")

# Positioning arguments (urutan harus sesuai)
perkenalan("Alice", 25, "Jakarta")

# Perkenalan arguments (urutan bebas)
perkenalan(kota="Bandung", nama="Bob", umur=30)
perkenalan(umur=20, kota="Surabaya", nama="Jack")

print("\n############ FUNC DENGAN BANYAK JENIS ############")
def buat_profil(nama, umur, kota="Jakarta", pekerjaan="Belum Bekerja"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"umur: {umur} tahun")
    print(f"Kota:" {kota})
    print(f"Pekerjaan:" {pekerjaan})
    print()

# Positioning + keyword arguments
buat_profil("Alice", 25) # Menggunakan default
buat_profil("Bob", 30, kota="Bandung")
buat_profil("Charlie", 28, pekerjaan="Developer")
buat_profil("Diana", 32, kota="Surabaya", pekerjaan="Designer")


print("\n############ LOCAL VARIABEL ############")
def fungsi_test():
    x = 10
    print("Nilai x dalam fungsi adalah : ", x)

fungsi_test()
# print(x) # ERROR KARENA X ADALAH LOCAL VARIABEL

print("\n############ GLOBAL VARIABEL ############")
nama_global = "Alice"

def tampilkan_nama():
    print("Nama: ", nama_global)

def ubah_nama():
    global nama_global
    nama_global = "Bob"

tampilkan_nama()
ubah_nama()
tampilkan_nama

