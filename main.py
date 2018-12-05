from Tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.QUIT = Button(self, text='Login', fg='red', command=self.test, font=("Arial", 15))
        self.QUIT.grid(ipadx = '50px')

    def test(self):
    	print 'this Ok'
    

root = Tk()
root.geometry("400x450")
app = Application(master=root)
app.mainloop()