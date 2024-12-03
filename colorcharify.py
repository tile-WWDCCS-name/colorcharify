from os.path import join, dirname
import argparse

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from tqdm import tqdm
import numpy as np

parser = argparse.ArgumentParser(description="这是一个能将图片转成汉字的脚本")
parser.add_argument('image_path', type=str,
                    help='输入图片的路径')
parser.add_argument('output_path', type=str,
                    help='输出图片的路径')
parser.add_argument('characters', type=str,
                    help='使用的字符')
parser.add_argument('-s', '--size', type=int, default=300,
                    help='横向字符个数，默认为300（不建议超过500）')
parser.add_argument('-cs', '--char_size', type=int, default=12,
                    help='单个字符的尺寸（高度），单位为像素，默认为12（建议在8~16之间）')
parser.add_argument('-fp', '--font_path', type=str, default=join((cur_dir := dirname(__file__)), 'font.ttf'),
                    help='字体路径，默认为此脚本所在的文件夹下的font.ttf文件，支持otf，但用otf会让速度变慢')
args = parser.parse_args()

image_path = args.image_path
output_path = args.output_path
size = args.size
char_size = args.char_size
font_path = args.font_path
characters = args.characters

font = ImageFont.truetype(font_path, char_size)
img = Image.open(image_path)
characters = [
    (char, font.getlength(char))
    for char in characters
]

width, height = img.size
aspect_ratio = height / width
img = img.resize((size, (height := round(size * aspect_ratio))))

img_rgba = img.convert('RGBA')
img_data = np.array(img_rgba)
bgc_r = round(255 - np.mean(img_data[:, :, 0]))
bgc_g = round(255 - np.mean(img_data[:, :, 1]))
bgc_b = round(255 - np.mean(img_data[:, :, 2]))
bgc = (round(bgc_r * 299/1000 + bgc_g * 587/1000 + bgc_b * 114/1000), ) * 3 + (255, )

img = Image.new('RGBA', (size * char_size, height * char_size), bgc)
draw = ImageDraw.Draw(img)

i = 0
x = 0
y = char_size
pixel_x = 0
pixel_y = 0
with tqdm(total=height) as pbar:
    while y <= height * char_size:
        pixel_x = int(x // char_size) - 1
        pixel_y = int(y // char_size) - 1
        char, length = characters[i % len(characters)]
        draw.text((x, y), char, tuple(img_data[pixel_y, pixel_x]), font, anchor='ls')
        x += length
        i += 1
        if x >= size * char_size:
            x = 0
            y += char_size
            pbar.update(1)

img.save(output_path)
