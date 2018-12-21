from Tkinter import *
from PIL import Image, ImageTk


class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.configure(bg='black')
        self.pack()
        self.createWidgets()


    def createWidgets(self):
    	self.button1 = Button(self,text='askfhvsduv')
    	self.button1.grid()
        