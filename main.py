from Tkinter import *
from PIL import Image, ImageTk
import home


class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.configure(bg='black')
        self.grid()
        self.createWidgets()


    def createWidgets(self):
    	self.user_name_ = Label(self,fg='#8bc900',bg='black', text='User Name:',font=("Arial", 15))
        self.user_name_.grid(sticky=W)
        
        self.user_name = Entry(self, font=("Arial", 15),fg='#8bc900')
        self.user_name.grid(pady=10, row= 0,padx=120)
        self.user_name.bind("<Return>",self.test_login)
        

    	self.password_ = Label(self,bg='black', text='Password  :',font=("Arial", 15),fg='#8bc900')
        self.password_.grid(sticky=W)
        
        self.password = Entry(self, font=("Arial", 15),show="-",fg='#8bc900')
        self.password.grid(row=1,pady=10)
        self.password.bind("<Return>",self.test_login)

        self.login = Button(self, text='Login', fg='red', command= self.test_login, font=("Arial", 15))
        self.login.grid(ipadx =70, rowspan=50)

    def test_login(self, *event):
    	if self.user_name.get() == 'admin' and self.password.get() == 'admin':
    		print 'Right Password'
    		self.activ_user()
    	else:
    		print 'Retry'

    def activ_user(self):
        self.forget()

        home.Application()
    	   		


    def test(self, *event):
    	u = self.user_name.get()
    	p = self.password.get()
    	print u+ '==>'+ p


