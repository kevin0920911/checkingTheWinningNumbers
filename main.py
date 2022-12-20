import tkinter 
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
# -*- coding: big5 -*-
# initialize

window_main = tk.Tk()

def transfer():
    time=box1.get()
    moddle=box2.get()
    if time=="本期" and moddle=="後三碼模式":
        os.system("python thisEasy.py")
    elif time=="上一期" and moddle=="後三碼模式":
        os.system("python nextEasy.py")
    elif time=="本期" and moddle=="全輸入模式":
        os.system("python thisAll.py")
    elif time=="上一期" and moddle=="全輸入模式":
        os.system("python nextAll.py")
    else:
        tkinter.messagebox.showinfo(title="錯誤", message="請輸入完整訊息")
   
window_main.title('對發票')

window_main.geometry('500x400')

window_main.resizable(1, 1)

window_main.iconphoto(True, tk.PhotoImage(file="img\icon.png"))


tk.Label(window_main, text='請輸入你想要對哪一期的發票',font=('Arial',20,'bold')).pack(anchor=tk.CENTER,padx=20, pady=10)

box1 = ttk.Combobox(window_main,font=('Arial',15), values=['本期','上一期'])

box1.pack(anchor=tk.CENTER,padx=20, pady=10)

tk.Label(window_main, text='請輸入你想要哪個模式',font=('Arial',20,'bold')).pack(anchor=tk.CENTER,padx=20, pady=10)

box2 = ttk.Combobox(window_main,font=('Arial',15),values=['後三碼模式','全輸入模式'])

box2.pack(anchor=tk.CENTER,padx=20, pady=10)

subimit = tk.Button(window_main, text='送出',font=('Arial',15,'bold'),command=transfer)     

subimit.pack(anchor=tk.CENTER,padx=20, pady=10)

window_main.mainloop()

