from PIL import Image, ImageChops
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()


file_path = filedialog.askopenfilename()


# RGBA to GAR channel swapping
# i figured out that its AGR (flipped XY)
image = Image.open(file_path)
r___, _g__, __b_, ___a = image.split()


image = Image.merge("RGB", (___a, _g__, r___))

R, G, B = image.split()

iamge = Image.merge("RGB", (R, G, B))

dir = file_path    # path to file without .png
splitdir = os.path.splitext(dir)[0]
image.save(splitdir + "_OpenGL_Converted" + ".png")
print("finished converting" + " Texture")
