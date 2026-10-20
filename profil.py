import json
import os

FILE_DATA = "data_ktp.json"

print("=== MENAMPILKAN PROFIL KTP ===")

if not os.path.exists(FILE_DATA):
    print("Belum ada data KTP yang terdaftar.")
else:
    with open(FILE_DATA, "r") as file:
        data = json.load(file)

    nik_cari = input("Masukkan NIK untuk melihat profil: ")

    ditemukan = False

    for pengguna in data:
        if pengguna["nik"] == nik_cari:
            print("\n======= PROFIL PENGGUNA =======")
            print("Nama lengkap  :", pengguna["nama"])
            print("NIK           :", pengguna["nik"])
            print("Tempat lahir  :", pengguna["tempat_lahir"])
            print("Tanggal lahir :", pengguna["tanggal_lahir"])
            print("Jenis kelamin :", pengguna["jenis_kelamin"])
            print("Alamat        :", pengguna["alamat"])
            print("Agama         :", pengguna["agama"])
            print("Pekerjaan     :", pengguna["pekerjaan"])
            print("===============================")

            ditemukan = True
            break

    if not ditemukan:
        print("Data dengan NIK tersebut tidak ditemukan.")