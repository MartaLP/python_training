import os
import os.path

biez_folder = os.getcwd()

# pliki = os.listdir('..\\')
pliki = os.listdir(biez_folder)

print('Pliki:')
print(pliki)

for plik in pliki:
    pelna_sciezka = os.path.join(biez_folder, plik)
    print(pelna_sciezka)
