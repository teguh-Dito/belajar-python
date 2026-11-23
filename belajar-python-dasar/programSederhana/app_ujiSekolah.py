# # Membaca soal dari file
# mengacak soal ujian
# mengacak posisi jawaban soal
# hasil score murid

def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
    
    import random 
    # acak soal
    random.shuffle(soal_asli)

    # soal = []
    soal_ujian = []
    # print(soal_asli)

    # for soal in soal_asli:
    for i in range(10):
        soal = soal_asli[i] # pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
        data = soal.split("|") # ["pertanyaan", jawaban1,jawaban2,jawaban3,jawaban4]
        pertanyaan = data[0] # pertanyaan
        semua_jawaban = data[1] # semua jawaban dalam string (not array)
        
        jawaban = semua_jawaban.split(",") # ["jawaban1", "jawaban2", "jawaban3", "jawaban4"]
        jawaban_benar = jawaban[0] # "jawaban1"

        # acak jawaban
        random.shuffle(jawaban) # ["jawaban2", "jawaban1", "jawaban3", "jawaban4"]

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })

        # print("Pertanyaan", pertanyaan)
        # print("Jawaban", jawaban)
        # print("Jawaban Benar", jawaban_benar)

    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    
    opsi = ["A", "B", "C", "D"]
    # for soal in soal_ujian:
    jawaban_benar = 0
    jawaban_salah = 0

    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan", i + 1, ":", soal["pertanyaan"])
        print("jawaban")

        # for jawaban in soal["jawaban"]:
        for j in range(len(soal["jawaban"])):
            # print(".", jawaban)
            jawaban = soal["jawaban"][j]
            print(opsi[j], ".", jawaban)

        jawaban_user = input("Pilih jawaban (A/B/C/D): ")
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("jawaban_benar")
            jawaban_benar += 1
        else:
            print("jawaban_salah")
            jawaban_salah +=1
    
    print("Hasil ujian")
    print("Jawaban benar: ", jawaban_benar)
    print("Jawaban salah: ", jawaban_salah)
    print("Hasil ujian: ", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")


app_ujian()
