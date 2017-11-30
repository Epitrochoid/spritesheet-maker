from math import ceil
from PIL import Image
from os import listdir

import sys

# python3 spritesheet-maker <dir> <num_wide> <x_dim> <y_dim> <out_name>

def main():
    all_files = listdir(sys.argv[1])
    png_files = [f for f in all_files if f.endswith('.png')]
    png_files.sort()
    num_wide = int(sys.argv[2])
    num_heigh = ceil(len(png_files) / num_wide)
    dimensions = (int(sys.argv[3]), int(sys.argv[4]))

    out_img = Image.new('RGBA', (num_wide * dimensions[0], num_heigh * dimensions[1]))

    cur_y = 0
    cur_x = 0
    for img_file in png_files:
        if (cur_x > num_wide):
            cur_x = 0
            cur_y += 1

        img = Image.open(img_file)
        out_img.paste(img, (cur_x * dimensions[0], cur_y * dimensions[1]))
        cur_x += 1

    out_img.save(sys.argv[5])

if __name__ == '__main__':
    main()
