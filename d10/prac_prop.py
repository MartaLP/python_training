class Pracownik(object):

    def __init__(self, name, stanowisko, pesel):
        self.imie = name
        self.stanowisko = stanowisko
        self.__pensja = None
        self.__pesel = pesel

    # getter
    @property
    def pensja(self):
        if self.__pensja is None:
            return 0
        else:
            return self.__pensja

    #print(p1.pensja)
    # p1.pensja = 3000
    # print(p1.pensja)

    #setter
    @pensja.setter
    def pensja(self, value):
        if isinstance(value, int):
            self.__pensja = value


if __name__ == '__main__':
    p1 = Pracownik('jan','kierownik','123233332')

p1.pensja = 3000
print(p1.pensja)