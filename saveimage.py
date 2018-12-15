from PIL import Image
import requests

url = "https://preview.redd.it/f2nq8n2vi2421.jpg?width=640&crop=smart&auto=webp&s=e42bd85329e446994745507280e190696e5378ae"
#save image
img_data = requests.get(url).content
with open('pics/dankmemes_1.jpg', 'wb') as handler:
    handler.write(img_data)

