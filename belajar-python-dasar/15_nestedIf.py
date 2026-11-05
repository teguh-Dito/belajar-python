username = input("Masukkan username Anda: ")
password = input("Masukkan password Anda: ")

if username == "admin":
    if password == "admin123":
        print("Login berhasil. Selamat datang, admin!")
    else:
        print("Password salah. Silakan coba lagi.")
else:
    print("Username tidak ditemukan. Silakan coba lagi.")