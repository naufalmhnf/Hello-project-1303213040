# deklarasikan variabel tabungan dengan type data list yang menyimpan data dengan type data dictionary yang akan digunakan untuk keperluan
tabungan = []

# baca file
with open("data_tabungan_mahasiswa.txt","r") as f:
    # pisahkan data teks dengan enter(\n), hasilnya akan berupa type data list
    result = f.read().split("\n")
    # setiap element pada result akan di olah
    for row in result:
        # pisahkan setiap kolom dengan spasi( )
        row = row.split(" ")
        # ambil data nama
        nama = row[0]
        # ambil data harga laptop
        harga_laptop = int(row[1])
        # ambil data total tabungan dengan menjumlah total minggu
        total_tabungan = 0
        for val in row[2:]:
            total_tabungan += int(val)
        # tambahkan data baru pada tabungan
        tabungan.append({
            "nama" : nama,
            "harga_laptop" : harga_laptop,
            "total_tabungan" : total_tabungan
        })

def terbanyak(data_list):
    max = 0
    nama = ""
    # telusuri semua data
    for data in data_list:
        # cek apakah total tabungan lebih besar dari max
        if data["total_tabungan"] > max:
            # jika lebih besar maka set variable menjadi data baru
            max = data["total_tabungan"]
            nama = data["nama"]
    # kembalikan nama
    return nama

def juara(data_list):
    # inisiasi nilai awal
    min = int(data_list[0]["harga_laptop"] - data_list[0]["total_tabungan"])
    nama = data_list[0]["nama"]
    # telusuri semua data
    for data in data_list:
        # hitung selisih harga laptop dan total tabungan
        selisih = data["harga_laptop"] - data["total_tabungan"]
        # cek apakah selisih lebih besar dari max
        if selisih < min:
            # jika lebih besar maka set variable menjadi data baru
            min = selisih
            nama = data["nama"]

    # tampilkan hasilnya
    print("mahasiswa dengan tabungan mendekati harga laptop adalah",nama)

def main():
    while True:
        print("Menu")
        print("1. Tampilkan Data Dictonary")
        print("2. Tampilkan mahasiswa dengan tabungan terbanyak")
        print("3. Tampilkan nama mahasiswa dengan tabungan paling mendekati harga laptop")
        print("4. exit")
        # masukan input user
        inp = int(input("Masukan pillihan: "))

        print("\n==========================================\n")
        # cek input user
        if inp == 1:
            print("===== Data Dictionary =====")
            # tampilkan semua data pada data tabungan
            for data in tabungan:
                print(data)
            print("\n==========================================\n")
        elif inp == 2:
            # panggil fungsi terbanyak
            result = terbanyak(tabungan)
            # tampilkan hasil
            print("mahasiswa dengan tabugan terbanyak adalah", result)
            print("\n==========================================\n")
        elif inp == 3:
            # panggil fungsi juara
            juara(tabungan)
            print("\n==========================================\n")
        elif inp == 4:
            break
        else:
            # jika input salah
            print("Input yang anda masukan salah!!!")
            print("\n==========================================\n")

# awal program
main()
# selesai
print("Program Berakhir")