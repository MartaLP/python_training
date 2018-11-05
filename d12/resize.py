import sys
from PIL import Image
import os

def resize_photo(width: int, name_root: str):
    file_folder = os.path.join(os.getcwd(), 'foto')
    files = os.listdir(file_folder)

    for index, file in enumerate(files):
        allowed_types = ['.jpg', '.png']

        file_ext = os.path.splitext(file)[1]
        if file_ext not in allowed_types:
            continue

        img_path = os.path.join(file_folder, file)
        pil_img = Image.open(img_path)

        # dodajemy assert zeby podpowiadalo funkcje dla zdjec
        assert isinstance(pil_img, Image.Image)
        # ratio
        ratio = width / pil_img.width

        new_height = int(pil_img.height) * ratio
        #resize
        resized = pil_img.resize((width, int(new_height)))
        new_file = f'{name_root}_{index}{file_ext}'
        new_name = os.path.join(file_folder, new_file)

        resized.save(new_name)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Podaj rozmiar, oraz nazwe!')
        exit(1)

    szerokosc = int(sys.argv[1])
    nazwa = sys.argv[2]

    resize_photo(szerokosc, nazwa)
