""" python script for wiki search from gui"""
import requests
import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title('Wikipedia')
win.geometry('300x100')

def serach_wiki():
	search = entry.get()
	result = wikipedia.summary(search)
	showinfo("Result ",result)

label = Label(win, text="Wikipedia Search :")
label.grid(row=0,column=0)

entry= Entry(win)
entry.grid(row=1,column=0)

button = Button(win, text="Search ",command=serach_wiki)
button.grid(row=1,column=1,padx=10)

win.mainloop()