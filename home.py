from Tkinter import *
from PIL import Image, ImageTk


class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
    	self.user_name_ = Label(self, text='User Name:',font=("Arial", 15))
        self.user_name_.grid(sticky=W)
        self.user_name_111 = Label(self, text='User Name:',font=("Arial", 15))
        self.user_name_111.grid(sticky=W)
        self.user_name_11 = Label(self, text='User Name:',font=("Arial", 15))
        self.user_name_11.grid(sticky=W)
        self.user_name_1 = Label(self, text='User Name:',font=("Arial", 15))
        self.user_name_1.grid(sticky=W)
    
    