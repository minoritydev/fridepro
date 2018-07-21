from tkinter import *
import pymysql
#database
db =  pymysql.connect(
    host='localhost',
    user='root',
    passwd='1337',
    db='fridepro'
)


window = Tk()
#fucntions

def onClickFill():
   
    windowFill= Tk()
    windowFill.title("test1")
    windowFill.geometry("500x500")
    vegSearchLabel = Label(windowFill, text="What are item(s) are you putting in?", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(windowFill, width=50, font=("Helvetica", 20)).place(x=0, y=60)
    fillBackBtn= Button(windowFill, text="Back", command=windowFill.destroy).place(x=0, y=450)
#function over

#main window
window.geometry("500x500")
window.title("test")
fillLbl = Label(window,text="Are you -", font=("Helvetica",10)).place(x=0,y=0)
fillBtn = Button(window, text="Filling in?", height=15, width=60, bg="#75d179", command=onClickFill,).place(x=0, y=20)
takeBtn = Button(window, text="Taking out?", height=17, width=60, bg="red", fg="white").place(x=0,y=250)

#main window over


window.mainloop()
