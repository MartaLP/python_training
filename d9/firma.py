from d9.pracownik import Pracownik

p1 = Pracownik('John Turturo', 'aktor',8000)
p2 = Pracownik('John Rambo', 'misjonarz',18000)

print(p1.roczna_podwyzka)
print(p2.roczna_podwyzka)

# Pracownik.roczna_podwyzka = 0.06
# print(p1.roczna_podwyzka)
# print(p2.roczna_podwyzka)

# Pracownik.ustaw_podwyzke(0.6)
# tak nie robic bo zmiana jest na poziomie klasy a nie instancji
p1.ustaw_podwyzke(0.001)
print(p1.roczna_podwyzka)
print(p2.roczna_podwyzka)
#
# print(f'Il prac: {Pracownik.il_pracownikow}')
#
# p3 = Pracownik('John Travolta', 'gwiazda', 15000)
# print(f'Il prac: {Pracownik.il_pracownikow}')
#
# del p1
# print('Koniec programu')

prawidlowy = Pracownik.sprawdz_pesel('99889988999')
# print(prawidlowy)