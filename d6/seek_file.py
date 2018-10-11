with open('lokomotywa.txt', encoding='utf-8') as file:
    tekst = file.read(30)
    print(tekst)
    print(file.readlines())

    pozycja = file.tell()
    print("obecna pozycja {}".format(pozycja))

    file.seek(0)
    pozycja = file.tell()
    print("obecna pozycja {}".format(pozycja))

    print(file.read())