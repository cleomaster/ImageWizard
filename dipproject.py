import cv2
import numpy as np
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Entry
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from tkinter.font import Font

def apply_filter():
    selected_option = option_var.get()
    img_result = img.copy()

    if selected_option == "Grayscale":
        img_result = cv2.cvtColor(img_result, cv2.COLOR_BGR2GRAY)
    elif selected_option == "Gaussian Blur":
        k = int(kernel_entry.get())
        img_result = cv2.GaussianBlur(img_result, (k, k), 0)
    elif selected_option == "Canny Edge Detection":
        t = int(kernel_entry.get())
        img_result = cv2.Canny(img_result, t, t)
    elif selected_option == "Dilation":
        k = int(kernel_entry.get())
        kernel = np.ones((k, k), np.uint8)
        img_canny = cv2.Canny(img_result, 100, 100)
        img_result = cv2.dilate(img_canny, kernel, iterations=1)
    elif selected_option == "Erosion":
        k = int(kernel_entry.get())
        kernel = np.ones((k, k), np.uint8)
        img_canny = cv2.Canny(img_result, 100, 100)
        img_result = cv2.erode(img_canny, kernel, iterations=1)

    display_image(img_result)


def display_image(image):

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_tk = ImageTk.PhotoImage(Image.fromarray(image_rgb))
    image_label.configure(image=img_tk)
    image_label.image = img_tk


def open_image():
    Tk().withdraw()
    filename = askopenfilename(title="Select an image file")
    global img
    img = cv2.imread(filename)
    display_image(img)

window = Tk()
window.title("DIP PROJECT")

bold_font = Font(family="Helvetica", size=12, weight="bold")
group_members_text = Label(window, font = bold_font, text = "Group Members:\nNabil FA20-BSE-009\nZeeshan FA20-BSE-016\nSADAT FA20-BSE-011\nHAMAD FA20-BSE-031")
group_members_text.pack()

image_label = Label(window)
image_label.pack()

open_button = Button(window, text="Open Image", command=open_image)
open_button.pack()

options = [
    "Grayscale",
    "Gaussian Blur",
    "Canny Edge Detection",
    "Dilation",
    "Erosion"
]
option_var = StringVar(window)
option_var.set(options[0])
option_dropdown = OptionMenu(window, option_var, *options)
option_dropdown.pack()

kernel_label = Label(window, text="Kernel Value:")
kernel_label.pack()
kernel_entry = Entry(window)
kernel_entry.pack()

apply_button = Button(window, text="Apply Filter", command=apply_filter)
apply_button.pack()




window.mainloop()