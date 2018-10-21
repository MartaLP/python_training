from silnik import Silnik

class Samochod(object):

    def __init__(self, silnik: Silnik):
        """
        Tworzy samochód.
        :param silnik: silnik samochodu
        """
        self.silnik = silnik


