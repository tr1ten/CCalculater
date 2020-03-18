from tkinter import *
import math
from PIL import ImageTk,Image
class calc:

    def replace(self):
        self.expression = self.var.get()
        self.replacedtxt = self.expression.replace(self.newdiv,'/')
        self.replacedtxt = self.replacedtxt.replace('x','*')

    def equal(self):
        self.replace()
        try:
            self.solved = str(eval(self.replacedtxt))

        except SyntaxError or NameError:
            self.var.delete(0,END)
            self.var.insert(0,'Invalid Input')

        else:
            self.var.delete(0,END)
            self.var.insert(0,self.solved)

    def sq(self):
        self.replace()
        try:
            self.newval = int(eval(self.replacedtxt))
        except SyntaxError or NameError:
            self.var.delete(0,END)
            self.var.insert(0,'Invalid Input ')

        else:
            self.sqval = math.pow(self.newval,2)
            self.var.delete(0,END)
            self.var.insert(0,self.sqval)
    def sqrt(self):
        self.replace()
        try:
            self.nval = int(eval(self.replacedtxt))
        except SyntaxError or NameError:
            self.var.delete(0,END)
            self.var.insert(0,'Invalid Input ')

        else:
            self.sqval = math.sqrt(self.nval)

            self.var.delete(0,END)
            self.var.insert(0,self.sqval)

    def clearall(self):
        self.var.delete(0,END)

    def clear(self):
        self.newtxt =self.var.get()
        self.newtxt = self.newtxt[0:-1]
        self.var.delete(0,END)
        self.var.insert(0,self.newtxt)

    def action(self,arg):
        self.var.insert(END,arg)
    def __init__(self,master):
        master.title("calculater by shubh")
        master.geometry()
        master.resizable(width=False,height=False)
        master.configure(bg='ivory3')
        self.image = ImageTk.PhotoImage(Image.open('wood.jpg'))
        self.div = '÷'
        self.ndiv = self.div.encode('utf-8',self.div)
        self.newdiv = self.ndiv.decode('utf-8')
        self.var = Entry(borderwidth=10,relief=SUNKEN,bg='saddlebrown',width=25,font=('Verdana',11),fg='grey3')
        self.var.grid(row=0,column=0,columnspan=6,stick='e,w',ipady=10)
        self.var.focus_get()
        self.font = 'glyphic 10 bold'
        Button(text='AC',compound=CENTER, command=lambda: self.clearall(),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=1, column=0)
        Button(text='C',compound=CENTER, command=lambda: self.clear(),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=1, column=1)
        Button(text='%', compound=CENTER,command=lambda: self.action('%'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=1, column=2)

        Button(text='1',compound=CENTER,command= lambda :self.action('1'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=4,column=0)
        Button(text='2',compound=CENTER, command=lambda: self.action('2'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=4, column=1)
        Button(text='3',compound=CENTER, command=lambda: self.action('3'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=4, column=2)
        Button(text='4',compound=CENTER, command=lambda: self.action('4'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=3, column=0)
        Button(text='5',compound=CENTER,command= lambda :self.action('5'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=3,column=1)
        Button(text='6',compound=CENTER, command=lambda: self.action('6'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=3, column=2)
        Button(text='7',compound=CENTER, command=lambda: self.action('7'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=2, column=0)
        Button(text='8', compound=CENTER,command=lambda: self.action('8'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=2, column=1)
        Button(text='9',compound=CENTER, command=lambda: self.action('9'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=2, column=2)
        Button(text='-',compound=CENTER, command=lambda: self.action('-'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=4, column=3)
        Button(text='0',compound=CENTER, command=lambda: self.action('0'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=5, column=1)
        Button(text=self.newdiv,compound=CENTER, command=lambda: self.action(self.newdiv),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=1, column=3)
        Button(text='X',compound=CENTER, command=lambda: self.action('x'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=2, column=3)
        Button(text='+',compound=CENTER, command=lambda: self.action('+'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=3, column=3)
        Button(text='-',compound=CENTER, command=lambda: self.action('-'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=4, column=3)
        Button(text='(',compound=CENTER, command=lambda: self.action('('),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=5, column=0)
        Button(text=')', compound=CENTER,command=lambda: self.action(')'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=5, column=2)
        Button(text='.',compound=CENTER, command=lambda: self.action('.'),image=self.image,font=self.font, height=46,width=30,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(row=5, column=3)
        Button(text='=', command=lambda: self.equal(),image=self.image,font=self.font,compound=CENTER, height=30,width=230,bg='white',borderwidth=5,relief=RAISED,fg='white').grid(columnspan=4,pady=3)


if __name__ == '__main__':
    root=Tk()
    newcal = calc(root)

    mainloop()