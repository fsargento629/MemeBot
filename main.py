from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from PIL import Image
import io


html = urlopen("https://www.reddit.com/r/dankmemes/")
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')},limit=10)
for image in images: 
    print(image['src']+'\n')

f = open("memes/dankmemes.txt","w+")
for image in images:
    f.write(image['src']+'\n')
print("Programa terminado")