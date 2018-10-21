from kod.d8.silnik import Silnik
from kod.d8.samochod import Samochod

# tworzymy instancję własnej klasy
v12 = Silnik(6000, 500)

# tworzymy instancję własnej klasy
# w której przechowujemy inny obiekt
dodge = Samochod(v12)

# tak dostajemy się do pól
# najpierw z samochodu wyciągamy silnik
# nastęnie z silnika - metodę tuninguj
dodge.silnik.tuninguj(20)
print(dodge.silnik.dodatkowa_moc)
