from Tkinter import *
from PIL import Image, ImageTk
import main , home


root = Tk()


root.maxsize(width=450, height=470)
root.minsize(width=450, height=470)
root.configure(background='#00ff38')
app = main.Application(master=root)
app.mainloop()