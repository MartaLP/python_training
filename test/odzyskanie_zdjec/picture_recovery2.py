import os
#
# jpg and png magic numbers (start of file, end of file)
file_types = [('jpg',b'\xff\xd8\xff',b'\xff\xd9'),
              ('png',b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a',b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82')]

def generate_pictures(text):
    for file_type in file_types:
        pos_end = 0
        while pos_end >= 0:
            pos_start = text.find(file_type[1],pos_end)
            if pos_start != -1:
                pos_end = text.find(file_type[2],pos_start)
                if pos_end != -1:
                # check whether there is additional sof between the start and end of the file
                    if text.find(file_type[1], pos_start+1, pos_end) != -1:
                        pos_end = text.find(file_type[1], pos_start+1, pos_end)
                        continue
                    pos_end = pos_end + len(file_type[2]) -1
                    save_piece_of_file(text,file_type[0],pos_start,pos_end)
            else:
                pos_end = -1
    print('Files recovered. Check them out!')

def save_piece_of_file(text,file_type,start,stop):
    if not os.path.exists('restored_pictures'):
        os.mkdir('restored_pictures')
    with open(f'restored_pictures/picture_{start}_{stop}.{file_type}', 'wb') as new_file:
        new_file.write(text[start:stop+1])

def restore_pictures(file_name):
    try:
        with open(file_name, 'rb') as file:
            generate_pictures(file.read())
    except FileNotFoundError:
        print(f'File "{file_name}" does not exist in the current path.')

restore_pictures('treasure_inside')
