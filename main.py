from PIL import Image, ImageDraw, ImageFont

from tkinter import Tk
from tkinter import filedialog

FILE_PATH = "Downloads"

main = Tk()
main.withdraw()
filename = filedialog.askopenfilename(initialdir=FILE_PATH, title="Select Your Image")


def water_mark(image, text):

    main_image = Image.open(image).convert("RGBA")

    watermark = Image.new("RGBA", main_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    w, h = main_image.size
    x, y = int(w / 2), int(h / 2)
    font = ImageFont.truetype("arial.ttf", int(w / 5))

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 100), anchor='ms')
    final = Image.alpha_composite(main_image, watermark)
    final.show()
    final.save('water_marked.png')


water_mark(filename, 'MeCoder')
