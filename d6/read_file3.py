with open('lokomotywa.txt', 'r', encoding='utf-8') as file:
    linijki = file.readlines()

    # print(linijki)
    for linia in linijki:
        print(linia, end='')