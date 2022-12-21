import nextSession 
import tkinter 
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pygame
import sys
from pygame.locals import *
import os
# -*- coding: big5 -*-
pygame.init()
pygame.mixer.init()
def process(event,s):
    input_.delete(0,'end')
    if len(s)==8:
        if s==number.nsa:
            pygame.mixer.music.load("music\win.wav") 
            pygame.mixer.music.play() 
            tkinter.messagebox.showinfo(title="中獎", message="你中了1000萬!")
        elif s==number.ns:
            pygame.mixer.music.load("music\win.wav") 
            pygame.mixer.music.play() 
            tkinter.messagebox.showinfo(title="中獎", message="你中了200萬!")
        else:
            for i in number.nb:
                if s == i:# 對中頭獎
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play() 
                    tkinter.messagebox.showinfo(title="中獎", message="你中了20萬!")
                    break
                if s[-7:] == i[-7:]:# 末七碼相同
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play()
                    tkinter.messagebox.showinfo(title="中獎", message="你中了4萬!")    
                    break
                if s[-6:] == i[-6:]:# 末六碼相同
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play()
                    tkinter.messagebox.showinfo(title="中獎", message="你中了1萬!") 
                    break
                if s[-5:] == i[-5:]:# 末五碼相同
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play()
                    tkinter.messagebox.showinfo(title="中獎", message="你中了4000!")   
                    break
                if s[-4:] == i[-4:]:# 末四碼相同
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play()
                    tkinter.messagebox.showinfo(title="中獎", message="你中了1000!")    
                    break
                if s[-3:] == i[-3:]:# 末三碼相同
                    pygame.mixer.music.load("music\win.wav") 
                    pygame.mixer.music.play()
                    tkinter.messagebox.showinfo(title="中獎", message="你中了200!")  
                    break
                
    else:
        tkinter.messagebox.showinfo(title="錯誤", message="格式錯誤")
class involce:
    def __init__(self,nsa,ns,nb):
        #特別獎
        self.nsa = nsa 
        #特獎
        self.ns = ns
        #頭獎
        self.nb = nb

number=involce(nextSession.number()[0],nextSession.number()[1],nextSession.number()[2])

window = tk.Tk()
window.title('對發票')
window.geometry('500x400')
window.resizable(1, 1)
window.iconphoto(True, tk.PhotoImage(file="img\icon.png"))

tk.Label(window, text='請輸入發票號碼(Enter送出)',font=('Arial',20,'bold')).pack(anchor=tk.CENTER,padx=20, pady=10)
input_ = tk.Entry(window, font=('Arial',20,'bold'))
input_.pack(anchor=tk.CENTER,padx=20, pady=10)

window.bind('<Return>',lambda x: process(x,input_.get()))
window.mainloop()