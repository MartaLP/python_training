class Zwierz(object):

    def __init__(self, nazwa, klasa):
        self.nazwa = nazwa
        self.klasa = klasa

    def ruszaj(self):
        print(f'Zwierz {self.nazwa} ruszyl sie.')


class Czlowiek(Zwierz):

    def __init__(self, imie, wiek):
        super().__init__(imie, 'kregowiec')
        # Zwierz().__init__(imie)
        self.imie = imie
        self.wiek = wiek

    def ruszaj(self):
        print(f'{self.nazwa} idzie.')

class Kot(Zwierz):

    def __init__(self, imie, kolor):
        super().__init__(imie, 'kregowiec')
        self.imie = imie
        self.kolor = kolor

    def daj_glos(self):
        print(f'{self.kolor} kot {self.imie} zrobil Miau.')

class Student(Czlowiek):

    def __init__(self, imie):
        super().__init__(imie, None)
        self.czy_glodny = True

    def nakarm(self):
        if self.czy_glodny:
            self.czy_glodny=False
            print(f'Student {self.imie} zostal nakarmiony.')
