from d9.fauna import Zwierz, Czlowiek, Kot, Student

z1 = Zwierz('pantofelek', 'bakterie')
z2 = Zwierz('dzdzownica', 'bezkregowce')

z1.ruszaj()
z2.ruszaj()

c1 = Czlowiek('Jan',22)
c1.ruszaj()

k1 = Kot('Ciapek','Szary')
k1.daj_glos()

s1 = Student('Marian')
print(s1.czy_glodny)
s1.nakarm()
print(s1.czy_glodny)

