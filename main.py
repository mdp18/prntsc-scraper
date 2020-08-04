### Multithreaded app
import webbrowser, random, string, requests, os, shutil
import requests
from bs4 import BeautifulSoup
import download

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}
numOfImages = input("How many images would you like to download? 1-1000: ")
txt_file = open("links.txt","a")

fileNames = []

randletter = 'abcdefghijklmnopqrstuvwxyz'

emptyTextFileBool = False

def emptyTextFile():
    file = 'links.txt'
    open(file, 'w').close()

def emptyFolder():
    shutil.rmtree("data/saved/")
    os.mkdir("data/saved/")

def scrape_and_store_image(inst_link):
    folderCheck()
    page = requests.get(inst_link, headers=hdr)
    soup = BeautifulSoup(page.content,'html.parser') #parses out the print.sc page
    link2 = soup.select('div img')[0] #Finds all div classes with img tags
    actualLink = link2['src'] #grabs the SRC tag of the first image div.
    if isValidLink(actualLink) == True: #checks the validity of the URL. If the URL starts with // inside of the image tag, it's a standard "image not found"
        fileName = actualLink[-21:]
        print(fileName)
        fileNames.append("data/saved/"+fileName)
        txt_file.write(actualLink + "\n")

def folderCheck():
    if os.path.isdir("data/saved/") == False:
        os.mkdir("data/saved/")
        os.mkdir('data/saved/imgur.com')

def isValidLink(str):
    if str[:2] == "//":
        return False
    else:
        return True

emptyTextFile()
emptyFolder()

for i in range(int(numOfImages)):
    rand = random.randrange(1000,9999)
    r1 = random.choice(randletter)
    r2 = random.choice(randletter)
    link = 'https://prnt.sc/' + r1 + r2 + str(rand)
    scrape_and_store_image(link)

txt_file.close()
## add downloading of the images after this line
#image = Image.open(fileNames[1])
#nsfw = classify(image) 

## Make sure to download the contents of the text file after this finishes running
download.DownloadImages()

#####checks for nudes in each image
print(fileNames)
print(len(fileNames))
