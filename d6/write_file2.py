baza = [
    "Adam,Kowalski,45,8000",
    "Anna,Wojtala,34,980",
    "Joanna,Mirko,67,7800"
]

# kopia_bazy = []
# for wpis in baza:
#     kopia_bazy.append(wpis + '\n')

# list comprehension
kopia_bazy = [wpis + '\n' for wpis in baza]

with open('baza.csv', 'w', encoding='utf-8') as file:
    file.writelines(kopia_bazy)

