import tkinter as tk
from pytube import YouTube
import os
 
def Download_Video():     
    url =YouTube(str(link.get()))
    availableClips = url.streams.filter(progressive=True, file_extension='mp4')
    video = availableClips.get_by_itag(22)
    video.download('Downloads')
    tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg=fgColor, bg=bgColor).place(x= 10 , y = 140)  

def Download_Audio():     
    yt = YouTube(str(link.get()))
    video = yt.streams.filter(only_audio=True).desc().first()
    out_file = video.download('Downloads')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    tk.Label(window, text = 'Your Audio is downloaded!', font = 'arial 15',fg=fgColor, bg=bgColor).place(x= 10 , y = 140) 


bgColor = "#404040"
fgColor = "#757575"
window = tk.Tk()
window.geometry("700x220")
window.config(bg=bgColor)
window.resizable(0,0)
window.title('YouTube Video Downloader')
 
link = tk.StringVar()
tk.Label(window,text = ' Youtube Video Downloader ', font ='arial 20 bold',fg="White", bg=bgColor).pack()
tk.Label(window, text = 'Paste Your YouTube Link Here:', font = 'arial 20 bold',fg=fgColor,bg=bgColor).place(x= 5 , y = 60)
link_enter = tk.Entry(window, width = 62,textvariable = link,font = 'arial 15 bold',bg=fgColor).place(x = 5, y = 110)
tk.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg=bgColor, bg =fgColor, padx = 2,command=Download_Video).place(x=485 ,y = 160)
tk.Button(window,text = 'DOWNLOAD AUDIO', font = 'arial 15 bold' ,fg=bgColor, bg =fgColor, padx = 2,command=Download_Audio).place(x=285 ,y = 160)
 
window.mainloop()
