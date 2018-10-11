with open('lokomotywa.txt', 'r', encoding='utf-8') as file:
    linijka = file.readline()
    print(linijka, end='')
    print(file.readline(),end='')