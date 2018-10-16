import os

# jpg and png magic numbers (start of file, end of file)
file_types = [('jpg',b'\xff\xd8\xff',b'\xff\xd9'),
              ('png',b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a',b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82')]

def find_pic_positions(text):
    pic_positions = []
    for file_type in file_types:
        pos_end = 0
        for i in range(text.count(file_type[1])):
            pos_start = text.find(file_type[1],pos_end)
            pos_end = text.find(file_type[2],pos_start)
            if pos_start == -1 or pos_end == -1:
                break
            else:
                #  check whether there is additional sof between the start and end of the file
                if text.find(file_type[1], pos_start+1, pos_end) != -1:
                    pos_end = text.find(file_type[1], pos_start+1, pos_end)
                    continue
                pos_end = pos_end + len(file_type[2]) -1
                pic_positions.append((file_type[0],pos_start,pos_end))
    if pic_positions == []:
        print('Files could not be found. Sorry!')
        exit()
    else:
        return pic_positions

def generate_pictures(text):
    # create a list with file types and their positions, e.g. [('png', 0,10), ('jpg', 11,50), ...]
    pic_positions = find_pic_positions(text)
    # create a folder for new files if it does not exist
    if not os.path.exists('restored_pictures'):
        os.mkdir('restored_pictures')
    # save the pieces of the original file as jpg or png files
    for index, elem in enumerate(pic_positions):
        with open(f'restored_pictures/picture_{index}.{elem[0]}', 'wb') as new_file:
            new_file.write(text[elem[1]:(elem[2]+1)])
    print('Files recovered. Check them out!')

def restore_pictures(file_name):
    try:
        with open(file_name, 'rb') as file:
            generate_pictures(file.read())
    except FileNotFoundError:
        print(f'File "{file_name}" does not exist in the current path.')

restore_pictures('treasure_inside')
