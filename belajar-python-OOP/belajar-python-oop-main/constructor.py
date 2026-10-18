class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def __str__(self):
        return f"Mahasiswa : {self.nim} - {self.nama} "

    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama


mhs = Mahasiswa(123456, "Arya")

print(mhs.nim)
print(mhs.nama)

print(f"Mahasiswa : {mhs}")

mhs2 = Mahasiswa(123457, "Arya")
print(mhs == mhs2)

class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo harus positif")

        self.no = no
        self.saldo = saldo

eko = BankAccount("1234567890", 100000)
# budi = BankAccount("1234567891", -100000) # error