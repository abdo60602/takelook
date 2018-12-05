from Tkinter import *

class takelook:
    def __init__(self, master):
        self.master = master
        master.title("Takelook")

    

root = Tk()
root.geometry("400x450")
my_gui = takelook(root)
root.mainloop()
