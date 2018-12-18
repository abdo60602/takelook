from Tkinter import *
from PIL import Image, ImageTk
import home


class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.configure(bg='black')
        self.grid()
        self.createWidgets()

        self.im = Image.open("pic.jpg")
        self.photo = ImageTk.PhotoImage(self.im)

        self.w = Label(self, 
                     compound = CENTER, 
                     image=self.photo,bg='black').grid()


    def createWidgets(self):
    	self.user_name_ = Label(self,fg='#8bc900',bg='black', text='User Name',font=("Arial", 15),padx=10)
        self.user_name_.grid(sticky=W)
        
        self.user_name = Entry(self, font=("Arial", 15),fg='#041633',borderwidth=2,relief='sunken')
        self.user_name.grid(pady=10, row= 0,padx=125)
        self.user_name.bind("<Return>",self.test_login)
        

    	self.password_ = Label(self,bg='black', text='Password',font=("Arial", 15),fg='#8bc900',padx=13)
        self.password_.grid(sticky=W)
        
        self.password = Entry(self, font=("Arial", 15),show="*",fg='#041633',borderwidth=2,relief='sunken')
        self.password.grid(row=1,pady=10)
        self.password.bind("<Return>",self.test_login)

        self.login = Button(self, text='Login', fg='white',bg='#8aa306', command= self.test_login, font=("Arial", 15,'bold'),borderwidth=4,relief='raised')
        self.login.grid(ipadx =40)

        self.forget = Button(self, text='Forget Password',bg='#5a5767', fg='white', command= self.test_login, font=("Arial", 10),borderwidth=3,relief='raised')
        self.forget.grid(padx=3)

    def test_login(self, *event):
    	if self.user_name.get() == 'admin' and self.password.get() == 'admin':
    		print 'Right Password'
    		self.activ_user()
    	else:
    		print 'Retry'

    def activ_user(self):
        self.destroy()

        home.Application()
    	   		


    def test(self, *event):
    	u = self.user_name.get()
    	p = self.password.get()
    	print u+ '==>'+ p


