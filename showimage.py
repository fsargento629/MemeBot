from PIL import Image
import io
from urllib.request import urlopen
fd = urlopen("https://i.redd.it/w6owupes91421.jpg")


image_file = io.BytesIO(fd.read())
im = Image.open(image_file)
im.size
