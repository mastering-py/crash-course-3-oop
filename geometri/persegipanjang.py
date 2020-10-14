class PersegiPanjang():
    # def __init__(self, p, l):
    #     self.p = p
    #     self.l = l

    # def info(self):
    #     return 'Modul Menghitung Luas Persegi Panjang'

    # def hitung_luas(self):
    #     return self.p * self.l

    def __init__(self, p, l):
        self.__p = p
        self.__l = l

    def info(self):
        print(f'Persegi panjang dengan panjang = {self.__p} dan lebar = {self.__l}')

    def set_hitung_luas(self, p, l):
        self.__p = p
        self.__l = l

    def get_hitung_luas(self):
        print(f'{self.__p * self.__l}')
