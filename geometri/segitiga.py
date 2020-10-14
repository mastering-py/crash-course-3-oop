class SegiTiga():
    # def __init__(self, alas, tinggi):
    #     self.alas = alas
    #     self.tinggi = tinggi
    #
    # def info(self):
    #     return 'Modul Menghitung Luas Segi Tiga'
    #
    # def hitung_luas(self):
    #     return self.alas * self.tinggi / 2

    def __init__(self, alas, tinggi):
        self.__alas = alas
        self.__tinggi = tinggi

    def info(self):
        print(f'Persegi panjang dengan panjang = {self.__alas} dan lebar = {self.__tinggi}')

    def set_hitung_luas(self, alas, tinggi):
        self.__alas = alas
        self.__tinggi = tinggi

    def get_hitung_luas(self):
        print(f'{self.__alas * self.__tinggi / 2}')