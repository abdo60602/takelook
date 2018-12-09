from Tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
    	self.user_name_ = Label(self, text='User Name:',font=("Arial", 15))
        self.user_name_.grid(sticky=W)
        
        self.user_name = Entry(self, font=("Arial", 15))
        self.user_name.grid(pady=10, row= 0,padx=120)
        self.user_name.bind("<Return>",self.test_login)
        

    	self.password_ = Label(self, text='Password  :',font=("Arial", 15))
        self.password_.grid(sticky=W)
        
        self.password = Entry(self, font=("Arial", 15),show="-")
        self.password.grid(row=1,pady=10)
        self.password.bind("<Return>",self.test_login)

        self.QUIT = Button(self, text='Login', fg='red', command= self.test_login, font=("Arial", 15))
        self.QUIT.grid(ipadx =165)

    def test_login(self, *event):
    	if self.user_name.get() == 'admin' and self.password.get() == 'admin':
    		print 'Right Password'
    	else:
    		print 'Retry'


    def test(self, *event):
    	u = self.user_name.get()
    	p = self.password.get()
    	print u+ '==>'+ p

root = Tk()
root.geometry("450x470")
app = Application(master=root)
app.mainloop()