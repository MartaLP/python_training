import os

jpg_start = b'\xff\xd8\xff'
jpg_end = b'\xff\xd9'

def start_stop_jpg(file):
    jpg_loc = []
    loc_end = -1
    for i in range(len(file)+1):
        loc_start = file.find(jpg_start,loc_end + 1)
        if loc_start == -1:
            break
        loc_end = file.find(jpg_end,loc_start + 1)
        jpg_loc.append((loc_start,loc_end))
    #print(jpg_loc)
    return jpg_loc

def generate_photos(file, jpg_locators):
    for jpg in jpg_locators:
        photo = file[jpg[0]:jpg[1]]
        if not os.path.exists('restored_photos'):
            os.makedirs('restored_photos')
        new_file = open('restored_photos/photo_{}_{}.jpg'.format(jpg[0],jpg[1]), 'wb')
        new_file.write(photo)
        new_file.close()

def restore_photos(binary_file):
    with open(binary_file, 'rb') as file:
        file_content = file.read()
        jpg_locators = start_stop_jpg(file_content)
        generate_photos(file_content, jpg_locators)

restore_photos('treasure_inside')
