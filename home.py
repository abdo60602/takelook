from Tkinter import *
from PIL import Image, ImageTk


class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.configure(bg='black')
        self.pack()
        self.createWidgets()


    def createWidgets(self):
    	self.user_name_1= Label(self, text='actiev',font=("Arial", 15))
        self.user_name_1.pack(ipadx=50,ipady=50)
        