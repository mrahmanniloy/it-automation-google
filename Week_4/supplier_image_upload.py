#!/usr/bin/env python3

import requests
import os

def main():
    source_path = '/home/<student-username>/supplier-data/images/'
    url = "http://localhost/upload/"

    for img in os.listdir(source_path):
        if not img.startswith('.') and 'jpeg' in img:
            im = os.path.join(source_path, img)
            with open(im, 'rb') as opened:
                r = requests.post(url, files={'file':opened})

if __name__ == "__main__":
    main()