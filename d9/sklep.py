#from towar import Towar
from d9.towar import Towar
# from pprint import pprint

t1 = Towar('lakierki', 'czarne', 23.00)
t2 = Towar('kapcie', 'zielone', 24.00)

print(t1)
print(t2)

zakupy = [t1, t2]
print(zakupy)

print(t1==t2)

wartosc = t1+ t2
print(wartosc)