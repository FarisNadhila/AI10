'''

Nama : Muhammad Faris Nadhila
Tugas 1 Basic Python
Soal No.3

'''

x = 70.0
praktek = 70
teori = 70

if teori >= x and praktek >= x:
    print ("Selamat, anda lulus!")
elif teori >= x and praktek < x:
    print ("Anda harus mengulang ujian praktek.")
elif teori < x and praktek >= x:
    print ("Anda harus mengulang ujian teori.")
else:
    print ("Anda harus mengulang ujian teori dan praktek.")

