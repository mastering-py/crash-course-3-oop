from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

# print('Encapsulation sederhana:')
# p1 = PersegiPanjang(10, 6)
# print(p1.info())
# print(p1.hitung_luas())

# print('-' * 50)

# s1 = SegiTiga(10, 6)
# print(s1.info())
# print(s1.hitung_luas())

# print('-' * 100)

print('Encapsulation menggunakan Get dan Set method dengan private Variable:')
p1 = PersegiPanjang(10, 6)  # nilai default dari panjang dan lebar persegi panjang
# print(p1.__p)  # variable p tidak bisa diakses karena bersifat private
p1.set_hitung_luas(20, 2)
p1.info()
p1.get_hitung_luas()

p1.set_hitung_luas(50, 2)
p1.info()
p1.get_hitung_luas()

print('-' * 50)

s1 = SegiTiga(10, 6)
s1.set_hitung_luas(30, 2)
s1.info()
s1.get_hitung_luas()

s1.set_hitung_luas(40, 2)
s1.info()
s1.get_hitung_luas()
