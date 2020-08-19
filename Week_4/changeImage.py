#!/usr/bin/env python3

import os
from PIL import Image

def main():
    source_path = "/home/<student-username>/supplier-data/images/"

    for img in os.listdir(source_path):
        if not img.startswith('.') and 'tiff' in img:
            try:
                input_path = os.path.join(source_path, img)
                new_path = os.path.splitext(input_path)[0]
                im = Image.open(input_path)
                final_path = '{}.jpeg'.format(new_path)
                im.convert("RGB").resize((600, 400)).save(final_path, "JPEG")
                im.close()
            except FileNotFoundError:
                pass

if __name__ == '__main__':
    main()