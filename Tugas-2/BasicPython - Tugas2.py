nama_kontak  = ["Fawwaz","John"]
nomor_kontak = ["08123456789", "08987654321"]

while True:
    print("Selamat Datang!\n")
    print("--- Menu ---")
    print("1. Daftar Kontak\n2. Tambah Kontak\n3. Keluar\n")
    menu = input("Pilih Menu: ")

    if menu=='1':
        print("Daftar Kontak")
        print("--------------------------")
        for x in range(len(nama_kontak)):
            print("Nama kontak  : {}\nNomor Kontak : {}\n".format(nama_kontak[x], nomor_kontak[x]))
        

    elif menu=='2':
        print("Mohon masukan data kontak:\n")
        print("--------------------------")
        nama  = input("Nama Kontak  : ")
        nomor = input("Nomor Kontak : ")
        nama_kontak.append(nama)
        nomor_kontak.append(nomor)
        print()
        print("Kontak berhasil ditambahkan!")
        print()
       

    elif menu=='3':
        print("Program selesai, sampai jumpa!")
        break

    else:
        print("Mohon maaf, menu tidak tersedia.")


