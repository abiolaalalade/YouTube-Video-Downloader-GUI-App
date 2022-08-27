from os import path
from tkinter import*
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
#allows us to copy files an dfolders and move them to whatever location the use wants to
import shutil

#fucntionality
def selectPath():
    #allows user to select path to send the download
    path = filedialog.askdirectory()
    pathLabel.configure(text=path)
def downloadFile():
    # Get user's path
    getLink = linkField.get()

    #get selected path
    userPath = pathLabel.cget('text')
    screen.title('Downloading....')

    #download video
    mp4Video = YouTube(getLink).streams.get_highest_resolution().download()
    #mp4Video = YouTube(getLink).streams.order_by("resolution").desc()[0].download()
    videoClip = VideoFileClip(mp4Video)
    videoClip.close()

    #move to selected directory
    shutil.move(mp4Video, userPath)
    screen.title('Download Complete! Download Another File')




############################# adding canvas,buttons, widgets, etc
#create screen
screen = Tk()
title = screen.title("Youtube Downloader")

#size of screen
canvas = Canvas(screen, width=700,height=700)
canvas.pack()
#canvas.configure(bg='white')

#import logo
imageLogo = PhotoImage(file='YTLogo.png')

#add image to canvas
#resize
imageLogo = imageLogo.subsample(1,1)
#set position
                     #x   y
canvas.create_image(350, 120, image=imageLogo)

#link field
linkField = Entry(screen, width=50)
linkLabel = Label(screen, text='Enter the YouTube Download Link:', font=('Arial',10))

#Select path for saving file
pathLabel = Label(screen, text='Select the path for the download', font=('Arial',10))
select_button = Button(screen, text='Select', command=selectPath)
#add to windows
canvas.create_window(350, 250, window=pathLabel)
canvas.create_window(350, 290, window=select_button)


#- add to widgest tot the window
canvas.create_window(350,200, window=linkLabel)
canvas.create_window(350,220, window=linkField)

#Download Buttons
downloadBtn = Button(screen, text='Download File',command=downloadFile)
canvas.create_window(350,330, window=downloadBtn)

############################# adding functionality


screen.mainloop()