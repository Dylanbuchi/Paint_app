import tkinter.ttk as ttk
import PIL

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageGrab, ImageTk


# setup the screen
root = Tk()
root.title("Paint App")
root.geometry("2000x2000")

#global variables
brush_color = "black"
canvas_color = "white"


# Functions:
# paint function: to draw on screen
def paint(event):

    # brush settings
    brush_width = int(slider.get())

    # brush types: BUTT, ROUND, PROJECTING
    brush = brush_type.get()

    # starting position
    x1 = (event.x - 1)
    y1 = (event.y - 1)

    # ending position
    x2 = (event.x + 1)
    y2 = (event.y + 1)

    # create lines to draw on screen
    canvas.create_line(x1, y1, x2, y2, fill=brush_color,
                       width=brush_width, capstyle=brush, smooth=TRUE)


# change the size of the brush
def change_brush_size(event):
    slider_label.config(text=int(slider.get()))


# change brush color
def change_brush_color():
    global brush_color
    brush_color = "black"
    brush_color = colorchooser.askcolor(color=brush_color)[1]


# change canvas color
def change_canvas_color():
    global canvas_color
    canvas_color = "black"
    canvas_color = colorchooser.askcolor(color=canvas_color)[1]
    canvas.config(bg=canvas_color)


# clear the screen
def clear_screen():
    canvas.delete(ALL)
    canvas.config(bg="white")


# save the drawing
def save():
    image_saved = filedialog.asksaveasfilename(
        initialdir="os", filetypes=(("png files", "*.png"),))

    if not image_saved.endswith(".png"):
        image_saved += ".png"

    # crop image only frm screenshot
    if image_saved:

        x = root.winfo_rootx()+canvas.winfo_rootx()
        y = root.winfo_rooty()+canvas.winfo_rooty()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(image_saved)

        # show message saved with success
        messagebox.showinfo("Image saved", "Image saved to " + image_saved)


# create canvas widget
w = 1800
h = 600
bg_color = "white"

canvas = Canvas(root, width=w, height=h, bg=bg_color)
canvas.pack(pady=20)


# capture mouse movements for painting
canvas.bind("<B1-Motion>", paint)

# create brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Controllers:
# brush size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush size")
brush_size_frame.grid(padx=50)

# brush slider
slider = ttk.Scale(brush_size_frame, from_=1, to=100,
                   command=change_brush_size, orient=VERTICAL, value=10)
slider.pack(pady=10, padx=10)

# brush slider label
slider_label = Label(brush_size_frame, text=slider.get())
slider_label.pack(pady=5)

# brush type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type")
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# radio buttons for brush type
brush_type_radio_1 = Radiobutton(
    brush_type_frame, text="1 Round", variable=brush_type, value="round")

brush_type_radio_2 = Radiobutton(
    brush_type_frame, text="2 Flat", variable=brush_type, value="butt")

brush_type_radio_3 = Radiobutton(
    brush_type_frame, text="3 Bright", variable=brush_type, value="projecting")

brush_type_radio_1.pack(anchor=W)
brush_type_radio_2.pack(anchor=W)
brush_type_radio_3.pack(anchor=W)

# change colors
color_frame = LabelFrame(brush_options_frame, text="Choose a Color")
color_frame.grid(row=0, column=2, padx=50)

# change brush color
brush_color_button = Button(
    color_frame, text="Brush Color", command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)


# change canvas background color
canvas_color_button = Button(
    color_frame, text="Background Color", command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

# program options:
options_frame = LabelFrame(brush_options_frame, text="Settings")
options_frame.grid(row=0, column=3, padx=50)

# clear screen button
clear_button = Button(options_frame, text="Clear Screen", command=clear_screen)
clear_button.pack(pady=10, padx=10)

# save drawing
save_button = Button(
    options_frame, text="Save your piece of art!", command=save)
save_button.pack(pady=10, padx=10)

root.mainloop()
