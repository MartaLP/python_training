class Kalk(object):

    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def pomnoz(self, a, b):
        wynik = a * b
        print(wynik)
