print("Program Penghitung Kalori Buah")
print("----------------------------------")
print("Buah              kalori/gram")
print("----------------------------------")
print("Anggur         66,9 kcal/100g")
print("Apel           52,1 kcal/100g")
print("Alpukat       160,1 kcal/100g")
print("Jeruk          47,1 kcal/100g")
print("Nanas            50 kcal/100g")
print("Semangka       88,7 kcal/100g")
print("Pisang         30,4 kcal/100g")
print("Stoberi        32,5 kcal/100g")
print("----------------------------------")

nama_buah     = []
nama_buah2    = []
kalori        = []
banyak_buah   = []
jumlah_harga  = []
jumlah_kalori = []

total_buah    = int(input("Total Buah yang dimakan : "))

for i in range(total_buah):
    print("Buah ke - ", i+1)
    nama_buah.append(input("Nama Buah               : "))
    banyak_buah.append(int(input("Banyak buah             : ")))

    if nama_buah[i] == "Anggur" or nama_buah[i] == "anggur":
        nama_buah2.append("Anggur")
        kalori.append(float(66.9))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Apel" or nama_buah[i] == "apel":
        nama_buah2.append("Apel")
        kalori.append(float(52.1))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Anggur" or nama_buah[i] == "anggur":
        nama_buah2.append("Anggur")
        kalori.append(float(66.9))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Alpukat" or nama_buah[i] == "alpukat":
        nama_buah2.append("Alpukat")
        kalori.append(float(160.1))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Jeruk" or nama_buah[i] == "jeruk":
        nama_buah2.append("Jeruk")
        kalori.append(float(47.1))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Nanas" or nama_buah[i] == "nanas":
        nama_buah2.append("Nanas")
        kalori.append(float(50))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Semangka" or nama_buah[i] == "semangka":
        nama_buah2.append("Semangka")
        kalori.append(float(88.7))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Pisang" or nama_buah[i] == "pisang":
        nama_buah2.append("Pisang")
        kalori.append(float(30.4))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    elif nama_buah[i] == "Stoberi" or nama_buah[i] == "stoberi":
        nama_buah2.append("Stoberi")
        kalori.append(float(32.5))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])
    else:
        nama_buah2.append("Kosong")
        kalori.append(float(0))
        jumlah_kalori.append(banyak_buah[i] * kalori[i])


print("\n------------------------------------------------------")
print("Hasil :")
print("------------------------------------------------------")
print("No. Nama       Banyak       Kalori      Total")
print("    Buah       Buah         Buah        Kalori")
print("------------------------------------------------------")

for a in range(total_buah):
    print (a+1, " ", nama_buah2[a],"   ", banyak_buah[a],"          ", kalori[a], "      ",jumlah_kalori[a])
    a = a + 1
print("------------------------------------------------------")
