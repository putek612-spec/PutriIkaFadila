print("hello python")
# ini adalah komentar
print("halo,")
print("selamat pagi!") # ini juga komentar

#printIn("statement ini tidak akan dipanggil")
nama = "noval"
hobi = 'makan'
umur = 18
laki = True
print("==== biodata ====")
print("nama: %s" % (nama))
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki))
pesan = 'halo, selamat pagi'
nilai_ujian = 99.2
nama ="noval"
umur = 18
nama = "noval agung"
umur = 21
nama: str = "noval"
hobi: str = 'makan'
umur: int = 18
laki: bool = True
nilai_ujian: float = 99.2
nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 21
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("rata-rata nilai: %f" % (nilai_rata_rata))
from typing import Final

PI: Final = 3.14
print("pi: %f" % (PI))

num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))