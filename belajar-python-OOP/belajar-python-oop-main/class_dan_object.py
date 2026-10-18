class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")


kampus1 = Kampus()
print(kampus1.nama)
print(kampus1.alamat)

kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "Eko"
mahasiswa1.perkenalan()
mahasiswa1.hello("Dian")

print(mahasiswa1.nim)
print(mahasiswa1.nama)

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 453534
mahasiswa2.nama = "Budi"
mahasiswa2.perkenalan()
mahasiswa2.hello("Dian")

print(mahasiswa2.nim)
print(mahasiswa2.nama)

print(type(mahasiswa1))
print(type(mahasiswa2))