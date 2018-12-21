from Tkinter import *
from PIL import Image, ImageTk
import main , home


root = Tk()
root.iconbitmap('logo.ico')
root.title('TakeLook')
root.maxsize(width=450, height=420)
root.minsize(width=450, height=420)
root.configure(background='black')
app = main.Application(master=root)
app.mainloop()