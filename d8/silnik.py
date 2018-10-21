class Silnik(object):
    """
    Silnik samochodowy
    """

    def __init__(self, pojemnosc, moc, paliwo='benzyna'):
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.czy_wlaczony = False
        self.paliwo = paliwo


    def wlacz(self):
        if not self.czy_wlaczony:
            self.czy_wlaczony = True

    def wylacz(self):
        if self.czy_wlaczony:
            self.czy_wlaczony = False

    def tuninguj(self, dodatkowa_moc):
        self.dodatkowa_moc = dodatkowa_moc
        self.moc += dodatkowa_moc

    def __str__(self):
        return f"Silnik {self.pojemnosc}, moc (km) {self.moc}"