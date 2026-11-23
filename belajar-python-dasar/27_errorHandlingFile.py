print("\n############ MENAMPILKAN DATA FILE ############")
try:
    with open("simpan_nilai.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File tidak ditemukan")

print("=== DATA SELESAI ===")