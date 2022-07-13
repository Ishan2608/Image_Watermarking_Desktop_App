from PIL import Image, ImageDraw, ImageFont

import tkinter as tk
from tkinter import filedialog
import random

FILE_PATH = "Downloads"
# ---------------------------------------------------------------------------------------------
# LOGIC
# ---------------------------------------------------------------------------------------------

filename = ""


def upload_file():
    global filename
    filename = filedialog.askopenfilename(initialdir=FILE_PATH, title="Select Your Image")
    file_upload_btn.config(fg='green')
    f = filename.split('/')[-1]
    uploaded_file_name.config(text=f)


def water_mark():
    global filename
    text = water_text.get()
    main_image = Image.open(filename).convert("RGBA")

    watermark = Image.new("RGBA", main_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    w, h = main_image.size
    x, y = int(w / 2), int(h / 2)
    font = ImageFont.truetype("arial.ttf", int(w / 7))

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 170), anchor='ms')
    final = Image.alpha_composite(main_image, watermark)

    f = filename.split('/')[-1]
    rand_id = random.random() * 1000000
    new_path = f'{f}_watermarked_{rand_id}.png'
    final.save(new_path)
    final.show()

    water_text.delete(0, tk.END)
    uploaded_file_name.config(text="")
    file_upload_btn.config(fg='black')


# ---------------------------------------------------------------------------------------------
# UI SETUP
# ---------------------------------------------------------------------------------------------
main = tk.Tk()
main.title('Water Mark your Image')

bg = tk.PhotoImage(file="background.png")
canvas = tk.Canvas(width=640, height=427)
img_bg = canvas.create_image(321, 215, image=bg)
button = canvas.create_text(321, 100, text='Water Mark Your Image. Just Type the Text', font=("Arial", 22, 'italic'), fill='white')

water_text = tk.Entry(fg="white", bg='black', font=('Arial', 12, 'bold'))
file_upload_btn = tk.Button(text="Upload", font=('Arial', 12, 'bold'), command=upload_file)
submit_btn = tk.Button(text='Submit', font=('Arial', 12, 'bold'), command=water_mark)

uploaded_file_name = tk.Label(text=" ", fg='white', bg='black',
                              font=('Arial', 12, 'bold'), wraplength=500)

canvas.grid(row=0, column=0, rowspan=18, columnspan=4)
water_text.grid(row=8, column=1, columnspan=2, sticky='nesw')
file_upload_btn.grid(row=9, column=1, sticky='nesw')
submit_btn.grid(row=9, column=2, sticky='nesw')
uploaded_file_name.grid(row=10, column=1, columnspan=2)

main.mainloop()
