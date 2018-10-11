with open('dane.csv', 'w', encoding='utf-8') as file:

    # exit(23)

    wpis = "Jan,Kowalski,34,3000.00\n"
    file.write(wpis)

    wpis2 = "Adam,Turek,45,8000.00"
    file.write(wpis2 + '\n')

