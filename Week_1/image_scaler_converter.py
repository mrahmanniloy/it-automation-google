#!/usr/bin/env python3

import os
from PIL import Image

def main():

    # Replace <student_user_name> with the username you get from qwiklabs
    source_dir = "/home/<student_user_name>/images/" 
    dest_dir = "/home/<student_user_name>/opt/icons/"

    for img in os.listdir(source_dir):
        # We need to check for period (.) as there is a .DS_Store file that throws error
        if '.' not in img[0]:
            try:
                input_path = os.path.join(source_dir, img)
                im = Image.open(input_path)
                im.rotate(-90).resize((128,128)).convert("RGB").save(dest_dir + img.split('.')[0], 'jpeg')
                im.close()
            except FileNotFoundError:
                pass

if __name__ == '__main__':
    main()