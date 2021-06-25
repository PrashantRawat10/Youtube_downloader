from tkinter import *
from pytube import YouTube


#Designing UI using tkinter module
root = Tk()
root.geometry('500x300')

root.title("DataFlair-youtube video downloader")

#adding labels
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#defining the main function
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'green', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()