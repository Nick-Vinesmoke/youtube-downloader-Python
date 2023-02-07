from tkinter import *
import customtkinter as ct
from PIL import ImageTk, Image
import pytube as pt
from tkinter import filedialog
import os


picture = 'files\picture.png'
icon = 'files\ico.ico'
textColor = '#7D7F81'
switch_var = 0
path1 = ''

def WinProperties(win):
    win.geometry("500x350+560+240")  # place and scale
    win.title("Youtube downloader")  # name of the window
    win.resizable(False, False)  # deformation of the window
    win.iconbitmap(f'{icon}')  # icon
    ct.set_appearance_mode('dark')
    ct.set_default_color_theme('blue')




def ChangeWar():
    global switch_var
    switch_var = 1




def StartWin():
    if switch_var == 0:
        global win
        win1 = ct.CTkToplevel(win)
        win1.geometry("320x150+680+380")
        win1.title("Info")  
        win1.resizable(False, False)  
        win1.iconbitmap(f'{icon}')  
        ct.set_appearance_mode('dark')
        ct.set_default_color_theme('blue')
        ct.CTkButton(master=win1, text='Download has been started!!!', font=('Berlin Sans FB', 24),
                     text_color_disabled=textColor, state=DISABLED, corner_radius=100, fg_color='#242424',
                     border_width=2,
                     border_color='#494949').place(relx=0.5, rely=0.3, anchor=CENTER)
        ct.CTkButton(master=win1, text='Ok', font=('Berlin Sans FB', 24), text_color=textColor, corner_radius=100,
                     fg_color='#5C5CC0', hover_color='#363670',
                     command=lambda: [ChangeWar(), win1.destroy(), Download()]).place(relx=0.5, rely=0.7, anchor=CENTER)
       


def EndWin():
    global switch_var
    switch_var = 0
    win2 = ct.CTkToplevel(win)
    win2.geometry("320x150+680+380")
    win2.title("Info")  
    win2.resizable(False, False)  
    win2.iconbitmap(f'{icon}')  
    ct.set_appearance_mode('dark')
    ct.set_default_color_theme('blue')
    ct.CTkButton(master=win2, text='Download has been finished!!!', font=('Berlin Sans FB', 24),
                 text_color_disabled=textColor, state=DISABLED, corner_radius=100, fg_color='#242424', border_width=2,
                 border_color='#494949').place(relx=0.5, rely=0.3, anchor=CENTER)
    ct.CTkButton(master=win2, text='Ok', font=('Berlin Sans FB', 24), text_color=textColor, corner_radius=100,
                 fg_color='#5C5CC0', hover_color='#363670', command=win2.destroy).place(relx=0.5, rely=0.7, anchor=CENTER)

def SelektPath():
    global path
    global path1
    path1 = filedialog.askdirectory()
    if path1 == '':
        path1 = os.path.abspath('files')
        path1 = path1[:-6]
        print(path1)

    path.set(path1)


def Download():
    global path
    global switch_var
    url = input.get()
    qual = quality.get()
    video = pt.YouTube(url)
    if qual == 'Quality':
        error = ct.CTkButton(master=win, text='Please select quality', font=('Berlin Sans FB', 24),
                     text_color_disabled=textColor, state=DISABLED, corner_radius=100, fg_color='#242424',
                     border_width=2, border_color='#494949')
        error.place(relx=0.5, rely=0.90, anchor=CENTER)
        error.after(1000, error.destroy)
    else:
        StartWin()
        if switch_var == 1:
            if qual == 'Height':
                downloadVideo = video.streams.get_highest_resolution()
            if qual == 'Low':
                downloadVideo = video.streams.get_lowest_resolution()
            downloadVideo.download(f'{path.get()}')
            EndWin()






win = ct.CTk()



quality = ct.StringVar(value="Quality")
path = ct.StringVar(value='Path for download')



WinProperties(win)#main window




canvas = ct.CTkCanvas(master=win,width=620, height=250, background='#242424', highlightthickness=0)
canvas.place(relx=0.5, rely=0.18, anchor=CENTER)
ct.CTkButton(master=win,text='Paste the link to the field below',font=('Berlin Sans FB', 24), text_color_disabled=textColor,state = DISABLED,corner_radius=100,fg_color='#242424',border_width=2,border_color='#494949').place(relx=0.5, rely=0.51, anchor=CENTER)
input = ct.CTkEntry(master=win,width=350,font=('Berlin Sans FB', 24), text_color=textColor,placeholder_text='link to the Youtube video',placeholder_text_color = '#363738',fg_color = '#494949')
input.place(relx=0.37, rely=0.63, anchor=CENTER)
combobox = ct.CTkComboBox(master=win,values=["Low", "Height"],variable=quality,text_color=textColor,font=('Berlin Sans FB',24),dropdown_font=('Berlin Sans FB',18),button_hover_color= '#494949',dropdown_text_color=textColor,)
combobox.place(relx=0.86, rely=0.63, anchor=CENTER)
buttonPath = ct.CTkButton(master=win,textvariable=path,font=('Berlin Sans FB', 16), text_color_disabled=textColor,state = DISABLED,fg_color='#242424',border_width=2,border_color='#494949',width=350,height=35)
buttonPath.place(relx=0.37, rely=0.75, anchor=CENTER)
ct.CTkButton(master=win,text='Select',font=('Berlin Sans FB',18), text_color=textColor, fg_color = '#5C5CC0',hover_color = '#363670',command=SelektPath,height=35).place(relx=0.86, rely=0.75, anchor=CENTER)
ct.CTkButton(master=win,text='Download',font=('Berlin Sans FB',24), text_color=textColor,corner_radius=100, fg_color = '#5C5CC0',hover_color = '#363670',command=Download).place(relx=0.5, rely=0.90, anchor=CENTER)
image = Image.open(f'{picture}')
image = image.resize((960, 540))
image = ImageTk.PhotoImage(image)
imagesprite = canvas.create_image(285, 150, image=image)


win.mainloop()

