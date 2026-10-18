import datetime

sekarang = datetime.datetime.now()
print("Sekarang", sekarang)

hari_ini = datetime.date.today()
print("Hari ini", hari_ini)

waktu_sekarang = datetime.datetime.now().time()
print("Waktu sekarang", waktu_sekarang)

ulang_tahun = datetime.date(2001, 10, 10)
print("Ulang tahun", ulang_tahun)

acara = datetime.datetime(2025, 10, 10, 20, 0, 0, 1)
print("Acara", acara)

print("Format panjang", sekarang.strftime("%A, %d %B %Y"))