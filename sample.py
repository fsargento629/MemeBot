from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.reddit.com/r/dankmemes/")
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')},limit=10)
for image in images: 
    print(image['src']+'\n')
