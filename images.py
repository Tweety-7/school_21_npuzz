from Printer import Printer
from PIL import Image

from PIL import ImageFont
from PIL import ImageDraw
from numpy import sqrt
from numpy.core.shape_base import hstack
from utils import check_file
from const import FONT_FILEPATH

import numpy as np
import PIL
from PIL import Image

FONT_SIZE = 400

def draw_digit(digit, font):
    W = 500
    H = 500
    img = Image.new('RGB', (W, H), (250,250,250))
    if digit == '0':
        return img
    msg = str(int(digit))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(msg, font=font)
    diff = 0
    while w >= W / 2 or h >= H / 2:
        diff += 5
        if diff >= FONT_SIZE:
            Printer.print_error_exit("Invalid digit tile size")
        font = ImageFont.truetype(FONT_FILEPATH, FONT_SIZE - diff)
        w, h = draw.textsize(msg, font=font)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="black", font=font)
    return img

def create_board(numbers, side, font):
    side_size = sqrt(len(numbers))
    images = [draw_digit(n, font) for n in numbers]
    images_splitted = [x.tolist() for x in np.array_split(images, side)]
    l = []
    for row in images_splitted:
        l.append(np.hstack(row))
    board = PIL.Image.fromarray(np.vstack(l))
    return board

def create_image(numbers):
    check_file(FONT_FILEPATH)
    font = ImageFont.truetype(FONT_FILEPATH, FONT_SIZE)
    side = sqrt(len(numbers))
    board = create_board(numbers, side, font)
    board.save('resources/default' + '.jpg')
