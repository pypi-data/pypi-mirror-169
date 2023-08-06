import flet
from flet import  Text, ElevatedButton, Page,TextField
from pytube import YouTube
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

os.path.join(BASE_DIR, "downloaded")
def sum(page: Page):
    page.bgcolor="yellow"
    page.title="Sherzodbek.Youtube.DL"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    url=TextField(label="URL")  
    def tom(e):
        page.bgcolor="yellow"
        yt = YouTube(url.value)
        print("Title: ",yt.title)
        ys = yt.streams.get_highest_resolution()
        print("Downloading...") 
        ys.download(filename="video.mp4", output_path="C:/downloaded")
        print("Download completed!!")

    page.add(
            url,
            
            ElevatedButton(
                text="Continue",
                width=200,
                height=100,
                on_click=tom
            )
        )
flet.app(target=sum)