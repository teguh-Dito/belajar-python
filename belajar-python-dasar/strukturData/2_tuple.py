point = (5, 10)
print(point)
print(point[0])
print(point[1])

# Untuk data yang tidak berubah 
tanggal_lahir = (15, 8, 1990)
print("Tanggal lahir: ", tanggal_lahir)

# iterasi di tuple
for e in tanggal_lahir:
    print(e)

# iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])
