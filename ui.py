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

valSearch=StringVar()
#fucntions

    
def onClickFill():
    val_search=StringVar()
    windowFill= Tk()
    windowFill.title("Fill")
    windowFill.geometry("500x500")
    vegSearchLabel = Label(windowFill, text="What are item(s) are you putting in?", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(windowFill, width=50, font=("Helvetica", 20), )
    vegSearchEntry.place(x=0, y=60)
    def temp():
        valSearch=vegSearchEntry.get()
        print(valSearch)
    fillBackBtn= Button(windowFill, text="Back", command=windowFill.destroy).place(x=0, y=450)
    fillOkBtn= Button(windowFill, text="Ok", command=temp).place(x=450, y=450)
    print("ok")

    
#function over
def onClickTake():
   
    windowFill= Tk()
    windowFill.title("Take")
    windowFill.geometry("500x500")
    vegSearchLabel = Label(windowFill, text="What are item(s) are you taking out?", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(windowFill, width=50, font=("Helvetica", 20)).place(x=0, y=60)
    fillBackBtn= Button(windowFill, text="Back", command=windowFill.destroy).place(x=0, y=450)


#main window
window.geometry("500x500")
window.title("Main Window")
fillLbl = Label(window,text="Are you -", font=("Helvetica",10)).place(x=0,y=0)
fillBtn = Button(window, text="Filling in?", height=15, width=60, bg="#75d179", command=onClickFill,).place(x=0, y=20)
takeBtn = Button(window, text="Taking out?", height=17, width=60, bg="red", fg="white", command=onClickTake).place(x=0,y=250)

#main window over


window.mainloop()

