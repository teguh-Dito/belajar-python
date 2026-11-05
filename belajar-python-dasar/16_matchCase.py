hari = input("Masukkan hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari libur")
    case _:
        print("Hari tidak valid")

# if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
#     print("Hari kerja")
# elif hari == "sabtu" or hari == "minggu":
#     print("Hari libur")
# else:
#     print("Hari tidak valid")