import os
import shutil
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube

# Function to select path for download
def select_path():
    selected_path = filedialog.askdirectory()
    path_label.config(text=selected_path)

# Function to download the file
def download_file():
    # Get user input link
    link = link_field.get()
    # Get selected path
    download_path = path_label.cget("text")
    # Update screen title
    screen.title("Downloading....")
    # Download video
    mp4_video = YouTube(link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # Move to selected directory
    shutil.move(mp4_video, download_path)
    # Update screen title
    screen.title("Download Complete! Download Another File")

# Create screen
screen = Tk()
screen.title("Youtube Downloader")

# Canvas
canvas = Canvas(screen, width=700, height=700)
canvas.pack()

# Logo
logo = PhotoImage(file="YTLogo.png").subsample(1, 1)
canvas.create_image(350, 120, image=logo)

# Link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter the YouTube Download Link:", font=("Arial", 10))

# Path selection
path_label = Label(screen, text="Select the path for the download", font=("Arial", 10))
select_button = Button(screen, text="Select", command=select_path)

# Widgets placement
canvas.create_window(350, 200, window=link_label)
canvas.create_window(350, 220, window=link_field)
canvas.create_window(350, 250, window=path_label)
canvas.create_window(350, 290, window=select_button)

# Download button
download_button = Button(screen, text="Download File", command=download_file)
canvas.create_window(350, 330, window=download_button)

# Start GUI
screen.mainloop()
