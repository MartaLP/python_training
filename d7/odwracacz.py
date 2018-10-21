def odwroc_zdanie(zdanie):
    return zdanie[::-1]

def drukuj_imie(imie):
    print(imie.capitalize())


def test():
    print(odwroc_zdanie('ala ma kota'))
    print(odwroc_zdanie('kajak'))


if __name__ == '__main__':
    test()