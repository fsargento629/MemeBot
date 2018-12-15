import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

window = tk.Tk()
#window.geometry("500x500") # (optional)    
imagefile = "pics/dankmemes_1.jpg"
img = ImageTk.PhotoImage(Image.open(imagefile))
lbl = tk.Label(window, image = img).pack()
window.mainloop()
