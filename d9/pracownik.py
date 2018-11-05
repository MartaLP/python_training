class Pracownik(object):

    il_pracownikow = 0
    roczna_podwyzka = 0.05

    def __init__(self, imie, stanowsiko, pensja):
        self.imie = imie
        self.stanowsiko = stanowsiko
        self.pensja = pensja
        Pracownik.il_pracownikow += 1

    @classmethod
    def ustaw_podwyzke(cls, wartosc):
        if cls.roczna_podwyzka + wartosc < cls.roczna_podwyzka * 1.1:
            cls.roczna_podwyzka = wartosc
        else:
            cls.roczna_podwyzka = cls.roczna_podwyzka * 1.08

    def __del__(self):
        Pracownik.il_pracownikow -= 1
        print(f'{self.imie} zostal usuniety')

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(pesel) != 11:
            return False
        return True
        # else:
        #     return True