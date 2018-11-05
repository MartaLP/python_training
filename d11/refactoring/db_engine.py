names_list = []

def search_name(name):
    '''
    Szuka podanego imienia w bazie. Zwraca True jeśli imię jest w bazie.

    (str) -> bool
    '''
    name = name.upper()
    return name in names_list

def add_to_base(name):
    '''
    Dodaje imię do bazy jeśli nie ma go w bazie. Gdy imie istnieje
    wyświetla komunikat.
    '''
    if not search_name(name):
        names_list.append(name.upper())
        print("Imię {} zostało dodane do kontaktów".format(name))
    else:
        print("Imię {} jest już w kontaktach".format(name))

def delete_name(name):
    '''Usuwa imie z bazy jesli imie w bazie jest'''
    if search_name(name):
        names_list.remove(name)
        print("Imię {} zostało usunięte".format(name))
    else:
        print("Brak imienia na liście")

def get_names_count():
    '''Drukuje liczbę imion w bazie'''
    print("Liczba imion na liście to {}".format(len(names_list)))

def print_names():
    '''Drukuje listę imion istniejących w bazie'''
    print(names_list)
