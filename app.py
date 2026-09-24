from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        #create db obj
        self.dbo=Database()
        self.apio= API()

        self.root = Tk()
        self.root.title("NLP")
        self.root.iconbitmap("resourses/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#3C27F5")

        self.login_gui()
        self.root.mainloop()



    def login_gui(self ):
        self.clear()
        heading = Label(self.root, text="Welcome to NLP", bg="#91F527",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font='verdana')

        label1 = Label(self.root, text="Enter your email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(10,10),ipady=3)

        label2 = Label(self.root, text="Enter your password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30,show="*")
        self.password_input.pack(pady=(10, 10), ipady=3)


        login_button=Button(self.root,text = 'Login',width=30,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))

        label3 = Label(self.root, text="not a member")
        label3.pack(pady=(10, 10))

        redirect_button = Button(self.root, text='Register Now',command=self.register_gui)
        redirect_button.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="Welcome to NLP", bg="#91F527", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('Verdana', 20))

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(10, 10), ipady=3)

        label1 = Label(self.root, text="Enter your email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(10, 10), ipady=3)

        label2 = Label(self.root, text="Enter your password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(pady=(10, 10), ipady=3)

        register_button = Button(self.root, text='Register', width=30, height=2,command=self.perform_regitration)
        register_button.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a member")
        label3.pack(pady=(10, 10))

        redirect_button = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_button.pack(pady=(10, 10))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_regitration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response==1:
            messagebox.showinfo(message="Successfully Registered")
        else:
            messagebox.showerror("Error",'Email already registered')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.search(email,password)

        if response==1:
            messagebox.showinfo(message="Successfully Logged In")
            self.home_gui()
        else:
            messagebox.showerror("Error",'Email/password incorrect')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="Welcome to NLP", bg="#91F527", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font='verdana')

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=2, command=self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))

        ner_button = Button(self.root, text='Name Entity Recognition', width=30, height=2,
                                  command=self.perform_regitration)
        ner_button.pack(pady=(10, 10))

        emotion_button = Button(self.root, text='Emotions predictions', width=30, height=2,
                                  command=self.perform_regitration)
        emotion_button.pack(pady=(10, 10))

        logout_button = Button(self.root, text='Logout', command=self.login_gui)
        logout_button.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="Welcome to NLP", bg="#91F527", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font='verdana')

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#91F527", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font='verdana')

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=30)
        self.sentiment_input.pack(pady=(10, 10), ipady=3)

        sentiment_button = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg="#91F527", fg="white")
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Reverse', command=self.home_gui)
        goback_button.pack(pady=(10, 10))


    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt


nlp = NLPApp()
