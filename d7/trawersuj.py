import os

path = r'C:\Users\ArkadioG\isapy8'

for current_folder, subfolders, files in os.walk(path):

    print(f'Bieżący folder: {current_folder}')

    for subfolder in subfolders:
        print(f'{subfolder}')

    for file in files:
        print(f"{file}")