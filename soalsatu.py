
total_ram = int(input("Masukan Kapasitas RAM : "))
total_petabit = int(input("Masukan Kapasitas Petabit : "))
kapasitas_so = int(input("Masukan Kapasitas Sistem Operasi : "))
kapasitas_ramsatu = int(input("Masukan Kapasitas Ram Program Satu : "))
kapasitas_ramdua = int(input("Masukan Kapasitas Ram Program Dua : "))

kapasitas_perpetabit = total_petabit - total_ram
ram_terpakai = kapasitas_so + kapasitas_ramsatu + kapasitas_ramdua 
ram_tidakterpakai = total_ram - ram_terpakai 
blok_satu = total_ram/total_ram
blok_dua = total_ram - kapasitas_perpetabit

print("======== HASIL ========")
print("Total Kapasitas Ram : ", total_ram)
print("Total Kapasitas Petabit : ", total_petabit)
print("Total Kapasitas per Petabit : ", kapasitas_perpetabit)
print("Total Ram Terpakai : ", ram_terpakai)
print("Total Ram Yang Tidak Terpakai : ", ram_tidakterpakai)
print("Jumlah Blok Yang Bernilai Satu : ", blok_satu)
print("Jumlah Blok Yang Bernilai Dua : ", blok_dua)

