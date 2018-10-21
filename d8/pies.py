class Pies(object):
    """Pies"""

    def __init__(self, imie, rasa, wiek):
        """
        Tworzy instancję klasy Pies
        :param imie: imię psa
        :param rasa: rasa psa
        :param wiek: wiek psa
        """

        # to są pola (zmienne) instancji
        self.name = imie
        self.breed = rasa
        self.age = wiek
        self.hungry = True
        self.color = None

    # to jest metoda (funkcja w klasie)
    def szczeknij(self, sila):
        """
        SPrawia że pies szczeka
        :param sila: moc szczekania
        :return: None
        """
        if sila < 6:
            print("Hauuuu")
        else:
            print("Haaaaaaauuuuuu")

    def nakarmij(self):
        """
        Karmi psa
        :return: None
        """
        self.hungry = False


    def __str__(self):
        """
        Tworzy string reprezentujący instancję Pies
        :return: str
        """
        return f"Pies {self.name}, ma {self.age} lat."


