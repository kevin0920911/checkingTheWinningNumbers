import tkinter as tk
from tkinter import ttk

# -*- coding: big5 -*-
# def a object : involece
class involece:
    def __init__(self,nsa,ns,nf):
        self.nsa=nsa
        self.ns=ns
        self.nf=nf

n = 0
def transfer():
    global n
    n = 1 if n==0 else n                     

# initialize

window_main = tk.Tk()

window_main.title('對發票')

window_main.geometry('500x400')

window_main.resizable(1, 1)

window_main.iconphoto(True, tk.PhotoImage(file="img\icon.png"))


tk.Label(window_main, text='請輸入你想要對哪一期的發票',font=('Arial',20,'bold')).pack(anchor=tk.CENTER,padx=20, pady=10)

box1 = ttk.Combobox(window_main,font=('Arial',15), values=['本期','這期'])

box1.pack(anchor=tk.CENTER,padx=20, pady=10)

tk.Label(window_main, text='請輸入你想要哪個模式',font=('Arial',20,'bold')).pack(anchor=tk.CENTER,padx=20, pady=10)

box2 = ttk.Combobox(window_main,font=('Arial',15),values=['後三碼模式','全輸入模式'])

box2.pack(anchor=tk.CENTER,padx=20, pady=10)

subimit = tk.Button(window_main, text='送出',font=('Arial',15,'bold'))     

subimit.pack(anchor=tk.CENTER,padx=20, pady=10,command=transfer)
if n==0:
    
else:
    

window_main.mainloop()

