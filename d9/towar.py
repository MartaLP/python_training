class Towar(object):

    def __init__(self, nazwa, kolor, cena):
        self.nazwa = nazwa
        self.kolor = kolor
        self.cena = cena

    def __str__(self):
        return f"But {self.nazwa} {self.kolor} cena: {self.cena}"

    def __repr__(self):
        return f"But {self.nazwa} - {self.cena}"

    def __eq__(self, other):
        if self.nazwa == other.nazwa and self.kolor == other.kolor:
            return True
        else:
            return False

    def __add__(self, other):
        return self.cena + other.cena
