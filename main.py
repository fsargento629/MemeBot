from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import csv
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

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

def DownloadImages(subreddit):
        pass




##### MAIN #####
meme_sources = CreateMemeSourcesList("subreddit_list.csv")
#dank_memes = subreddit("https://www.reddit.com/r/dankmemes/","dankmemes",-100)
#ScrapeImages(dank_memes,str(datetime.datetime.today()))

#for meme_source in meme_sources:
        #ScrapeImages(meme_source.url,str(datetime.datetime.today()))
for meme_source in meme_sources:
         print(meme_source.name +" "+ str(meme_source.meme_count))
         print("--------------")
         ScrapeImages(meme_source,str(datetime.datetime.today()))