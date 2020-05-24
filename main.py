import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

def getOnlyNames(file):
    file1 = open(file, 'r', encoding='utf8')
    Lines = file1.readlines()

    count = 0
    names = ""
    for line in Lines:
        if count % 3 == 0:
            names += line.strip() + " "
        count+=1
    return names

def generateWordCloud(string, image):
   maskArray = npy.array(Image.open(image))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("final.png")


names = getOnlyNames('memorial.txt').lower()
generateWordCloud(names, 'bolsonaro.png')

print(names)
