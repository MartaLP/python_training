from dzien8.Refactoring.db_engine import *

WELCOME_MESSAGE = """Baza danych
Wybierz opcję:
Wyszukaj imie, naciśnij klawisz 1:
Dodaj imie, naciśnij klawisz 2:
Usuń imie, naciśnij klawisz 3:
Wyświetl liczbę imion, naciśnij klawisz 4:
Wyświetl listę imion, naciśnij klawisz 5:
Zakończ program, naciśnij klawisz 0:\n"""

# wyswietlamy listę poleceń
response = input(WELCOME_MESSAGE)

while response != "0":
    if response == "1":
        name = input("Podaj wyszukiwane imię: ")
        if search_name(name):
            print("Imię {} jest już w kontaktach".format(name))
        else:
            print("Imię {} nie zostało odnalezione".format(name))
    elif response == "2":
        add_to_base(input("Dodaj imię do listy: "))
    elif response == "3":
        delete_name(input("Podaj imię, które chcesz usunąć: "))
    elif response == "4":
        get_names_count()
    elif response == "5":
        print_names()
    else:
        print("Podałeś złę polecenie, spróbuj ponownie.")

    response = input("Podaj nowe polecenie\n")
