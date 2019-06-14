from tkinter import *
from tkinter import messagebox
from .Spammer import WhatsAppSpammer
from tkinter import filedialog
import webbrowser
class MainUIClass():
    def __init__(self):
        self.rootr=Tk()
        self.rootr.title("WhatsApp Spammer")
        self.rootr.iconbitmap("files/Martz90-Hex-Whatsapp.ico")
        self.root=Frame(self.rootr)
        self.root.grid(row=0)
        self.root.configure(background="lightgreen")
        Label(self.root,text="Name of the target: ",font=("Consolas 12"),bg="lightgreen").grid(row=0,column=0,pady=5)
        self.TargetName = Entry(self.root,font=("Consolas 12"),borderwidth=3)
        self.TargetName.grid(row=0,column=1)
        Label(self.root,text="Message: ",font=("Consolas 12"),bg="lightgreen").grid(row=1,column=0,pady=5)
        self.TargetMessage = Entry(self.root,font=("Consolas 12"),borderwidth=3)
        self.TargetMessage.grid(row=1,column=1)
        Label(self.root,text="Number of messages: ",font=("Consolas 12"),bg="lightgreen").grid(row=2,column=0,pady=5)
        self.NumberOfMessages = Entry(self.root,font=("Consolas 12"),borderwidth=3)
        self.NumberOfMessages.grid(row=2,column=1)
        Label(self.root,text="Time interval b/w messages: ",font=("Consolas 12"),bg="lightgreen").grid(row=3,column=0,pady=5)
        self.TimeInterval = Entry(self.root,font=("Consolas 12"),borderwidth=3)
        self.TimeInterval.grid(row=3,column=1)
        self.Chromedriverpath = Entry(self.root,font=("Consolas 12"),borderwidth=3)
        self.Chromedriverpath.grid(row=4,column=1)
        self.Chromedriverchoose = Button(self.root,font=("Consolas 12 bold"),fg="blue",bg="lightblue", text="Choose Chrome webdriver",command=self.chromedrivchoose)
        self.Chromedriverchoose.grid(row=4,column=0,pady=5)
        self.root1=Frame(self.rootr)
        self.root1.grid(row=1)
        self.Reset = Button(self.root1,bg="lightblue",font=("Consolas 12 bold"), text="Reset", fg="green", command=self.reset)
        self.Reset.grid(row=0,column=0,sticky="w",ipadx=20,padx=50,pady=10)
        self.Spam = Button(self.root1,bg="lightblue",font=("Consolas 12 bold"),text="Spam",fg="red",command=self.run)
        self.Spam.grid(row=0,column=1,sticky="e",ipadx=20,padx=50,pady=10)
        self.link1 = Label(self.root1, text="Developed by Neeramitra Reddy",borderwidth=3, relief=SUNKEN,fg="blue", cursor="hand2")
        self.link1.grid(row=1,columnspan=6,sticky="ew")
        self.link1.bind("<Button-1>", lambda e: self.callback("https://github.com/neeru1207"))
        self.root.mainloop()
    def chromedrivchoose(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Choose Chrome webdriver", filetypes = (("Exec files","*.exe"),("All files","*.*")))
        self.Chromedriverpath.delete(0,END)
        self.Chromedriverpath.insert(0,filename)
    def callback(self,url):
        webbrowser.open_new(url)
    def reset(self):
        self.TargetName.delete(0,END)
        self.TimeInterval.delete(0,END)
        self.NumberOfMessages.delete(0,END)
        self.TargetMessage.delete(0,END)
    def run(self):
        Nummes = 0
        Timint = 0
        if self.TargetName.get()=="" or self.TargetMessage.get()=="" or self.TimeInterval=="" or self.NumberOfMessages=="":
            messagebox.showerror("ERROR","One or more fields empty!")
            return -1
        try:
            Nummes = int(self.NumberOfMessages.get())
        except:
            messagebox.showerror("ERROR","Number of messages has to be an integer!")
            return -1
        try:
            Timint = int(self.TimeInterval.get())
        except:
            messagebox.showerror("ERROR","The Time interval has to be an integer!")
            return -1
        if Nummes <0:
            messagebox.showerror("ERROR","The number of messages can't be negative!")
            return -1
        if Timint <0:
            messagebox.showerror("ERROR","The time interval cannot be negative!")
            return -1
        if self.Chromedriverpath.get()=="":
            messagebox.showerror("ERROR","No Chrome Webdriver selected!")
            return -1
        targname = '"'+self.TargetName.get()+'"'
        targmes = self.TargetMessage.get()
        try:
            x = WhatsAppSpammer(ChromeWebDriverPath=self.Chromedriverpath.get(), TargetName=targname,
                            TargetMessage=targmes, NumberOfMessages=Nummes, TimeInterval=Timint)
        except:
            messagebox.showerror("ERROR","Invalid Chrome webdriver location!")
            return -1
        try:
            x.run()
        except:
            messagebox.showerror("ERROR","Invalid target name!")
            return -1
        messagebox.showinfo("SUCCESS","Successfully spammed the message!")