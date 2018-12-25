from urllib.request import urlopen
import os
from bs4 import BeautifulSoup
import re
import datetime
import csv
from itertools import cycle
import io
import requests
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)


#Definicao de app, copiado da net: (nao mexer!)
class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''

    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay

        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((self.photo_image(image), image) for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        '''cycle through the images and show them'''

        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)


    def photo_image(self, jpg_filename):

        with io.open(jpg_filename, 'rb') as ifh:
            pil_image = Image.open(ifh)
            return ImageTk.PhotoImage(pil_image)

    def run(self):
        self.mainloop()



#def de subreddit

class subreddit:
    
    average_grade = 0
    def __init__(self,url,name,meme_count):
        self.url = url
        self.name = name
        self.meme_count = meme_count

def CreateMemeSourcesList(file_name):
        sources = []
        with open(file_name,"r") as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                        try:
                               with open("memes/"+line[1]+".csv") as f:
                                        for i, l in enumerate(f):
                                                pass
                               sources.append(subreddit(line[0],line[1],i+1))
                        
                                
                        except :
                                sources.append(subreddit(line[0],line[1],0))                         
       
   
        
        return sources
                        


def ScrapeImages(subreddit,date):   
    f = open("memes/"+subreddit.name + ".csv","a")
    html = urlopen(subreddit.url)
    
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')},limit=10)
    for image in images:
        subreddit.meme_count = subreddit.meme_count +1
        print(image['src'])
        f.write(date + "," + image['src'] + ","+ str(subreddit.meme_count) + "\n")

def DownloadImage(subreddit,id,url):
        
        #save image
        img_data = requests.get(url).content
        with open('pics/'+subreddit.name+"_"+str(id)+".jpeg", 'wb') as handler:
                handler.write(img_data)
        with open('pics/'+subreddit.name+".csv","a") as log_file:
                log_file.write(id+","+ str(datetime.datetime.today()))

def CriarListaMemes():
        lista_de_memes = os.listdir("pics")
        lista_de_memes_refinada = []
        for meme in lista_de_memes:
                if meme.split(".")[1]!="jpeg" :
                        lista_de_memes.remove(meme)
                else:
                        #mudar diretoria atras
                        lista_de_memes_refinada.append("pics/"+meme)

        return lista_de_memes_refinada

##### MAIN #####
meme_sources = CreateMemeSourcesList("subreddit_list.csv")
#dank_memes = subreddit("https://www.reddit.com/r/dankmemes/","dankmemes",-100)
#ScrapeImages(dank_memes,str(datetime.datetime.today()))

#for meme_source in meme_sources:
        #ScrapeImages(meme_source.url,str(datetime.datetime.today()))
for meme_source in meme_sources:
         print(meme_source.name +" "+ str(meme_source.meme_count))
         print("--------------")
         #ScrapeImages(meme_source,str(datetime.datetime.today()))
# code to download images:

for meme_source in meme_sources:
        saved_memes = []
        known_memes = []
        
        with open("pics/"+meme_source.name+".csv","r+") as saved_memes_file:
                with open("memes/"+meme_source.name+".csv","r+") as known_memes_file:
                        saved_memes_reader = csv.reader(saved_memes_file)
                        known_memes_reader = csv.reader(known_memes_file)
                        for saved_meme in saved_memes_reader:
                                saved_memes.append(saved_meme[0])
                        for known_meme in known_memes_reader:
                                known_memes.append([ known_meme[1],known_meme[2] ] )  #url and id
                        for meme in known_memes:
                                if not (meme[1] in saved_memes):
                                        #DownloadImage(meme_source,meme[1],meme[0])
                                        pass
                                

lista_de_memes = CriarListaMemes()
app = App(lista_de_memes, 50, 100, 3500)
app.show_slides()
app.run()