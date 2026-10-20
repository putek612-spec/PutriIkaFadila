import json
import os

FILE_DATA = "data_ktp.json"

print("=== REGISTRASI DATA KTP ===")

nama = input("Masukkan nama lengkap: ")
nik = input("Masukkan NIK: ")
tempat_lahir = input("Masukkan tempat lahir: ")
tanggal_lahir = input("Masukkan tanggal lahir: ")
jenis_kelamin = input("Masukkan jenis kelamin: ")
alamat = input("Masukkan alamat: ")
agama = input("Masukkan agama: ")
pekerjaan = input("Masukkan pekerjaan: ")

# Membaca data yang sudah tersimpan
if os.path.exists(FILE_DATA):
    with open(FILE_DATA, "r") as file:
        data = json.load(file)
else:
    data = []

# Memeriksa apakah NIK sudah terdaftar
if any(pengguna["nik"] == nik for pengguna in data):
    print("\nNIK sudah terdaftar!")
else:
    pengguna = {
        "nama": nama,
        "nik": nik,
        "tempat_lahir": tempat_lahir,
        "tanggal_lahir": tanggal_lahir,
        "jenis_kelamin": jenis_kelamin,
        "alamat": alamat,
        "agama": agama,
        "pekerjaan": pekerjaan
    }

    data.append(pengguna)

    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)

    print("\nRegistrasi berhasil!")
    print("Data KTP berhasil disimpan.")