```python 
from youtubepy import *
from pytube import YouTube
import eel
from pywebio import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

eel.init("web")
#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
eel.start("index.html")


start_server( port=8080)
