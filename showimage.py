<<<<<<< HEAD
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

window = tk.Tk()
#window.geometry("500x500") # (optional)    
imagefile = "pics/dankmemes_1.jpg"
img = ImageTk.PhotoImage(Image.open(imagefile))
lbl = tk.Label(window, image = img).pack()
window.mainloop()
=======
from PIL import Image
import io
from urllib.request import urlopen
fd = urlopen("https://i.redd.it/w6owupes91421.jpg")


image_file = io.BytesIO(fd.read())
im = Image.open(image_file)
im.size
>>>>>>> 0cc4da18f6c18658f9d0a10f1402eafeaa929a9e
