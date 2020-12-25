import tkinter as tk
from pytube import YouTube as yt


#where to save 
SAVE_PATH = 'C:\\Users\\User\\Downloads\\'



def downloadVid():
    global entry
    link =entry.get()
    try:
        yt(link).streams.first().download(SAVE_PATH)
    except:
        print('An error occurred')
    print(yt(link).title + ' successfully downloaded!')

#root   
root=tk.Tk()

#give the box a label (title)
label=tk.Label(root,text="Youtube Downloader")
label.pack()

#receive input
entry=tk.Entry(root,bd=5)
entry.pack(side=tk.TOP)

#download button
button=tk.Button(root,text="Download",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()
