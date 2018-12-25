import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/
window = tk.Tk()

imagefile = "dankmemes_14.jpeg"
img = ImageTk.PhotoImage(Image.open(imagefile))
tk.Label(window, image = img).pack()

window.mainloop()