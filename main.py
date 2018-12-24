from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import csv
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)
import requests
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
                                        DownloadImage(meme_source,meme[1],meme[0])
                                

