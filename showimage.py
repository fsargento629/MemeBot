import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

window = tk.Tk()
#window.geometry("500x500") # (optional)    
imagefile = "pics/dankmemes_5.jpeg"
img = ImageTk.PhotoImage(Image.open(imagefile))
tk.Label(window, image = img).pack()
window.mainloop()

    