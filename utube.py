from tkinter import *
from pytube import YouTube 

import sys

root = Tk()

root.geometry('500x500')
def download_progress():#just a simple function i have created 
    a = f'{url1.get()}'
    get_link = YouTube(a)

    
    all_format = get_link.streams.order_by('resolution').desc()
    #for format_i in all_format:
        #print(all_format)
    filter_video = all_format.filter(file_extension = 'mp4',resolution = '720p',progressive = True)
    print('Available resoltion In This video')
    available_resolution = []
    format_available_resolution = []
    for filters_videos in all_format:

        f = filters_videos.resolution
        available_resolution.append(f)
        for repeat_none in available_resolution:

            if repeat_none in  format_available_resolution:
                pass
        
            else:
                 format_available_resolution.append(repeat_none)
            
    print(format_available_resolution)
    filter_video.first().download(r'C:\Users\JOKER\AppData\Local\Programs\Python\Python38')
        

    
url1 = StringVar()


label = Label(root,text = "Enter Youtube Url" , font = ("",15))
label.grid(row = 0,column = 0)

entry = Entry(root , textvariable = url1)
entry.grid(row = 0,column = 1,padx = 20,pady = 20 )
btn = Button(root , text ="DOWNLOAD",command = download_progress)
btn.grid(row=1,column =1) 
root.mainloop()
