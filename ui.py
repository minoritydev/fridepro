from tkinter import *
import pymysql
#database
db =  pymysql.connect(
    host='localhost',
    user='root',
    passwd='1337',
    db='fridepro'
)
cursor=db.cursor()

window = Tk()

valSearch=StringVar()
valQty=IntVar()
#fucntions

    
def onClickFill():
    val_search=StringVar()
    windowFill= Tk()
    windowFill.title("Fill")
    windowFill.geometry("500x500")
    vegSearchLabel = Label(windowFill, text="What are item(s) are you putting in?", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(windowFill, width=50, font=("Helvetica", 20), )
    vegSearchEntry.place(x=0, y=60)
    
    #getNameFromDB will fetch entered name from DB (if it exsists) 
    def getNameFromDB():
        valSearch=vegSearchEntry.get()
        #print(valSearch)
        
        def quantityWindow(): #opens new window to enter quantity of item
            cursor.execute("select quantity from vegetables where name=%s",valSearch)
            quantity = cursor.fetchall()
            windowQty= Tk()
            windowQty.title("Enter Amount to Fill")
            windowQty.geometry("500x500")
            vegQtyInputLabel = Label(windowQty, text=("How many "+valSearch+" will you put in?"), font=("Helvetica", 22)).place(x=0,y=0)
            vegPresentQtyLabel = Label(windowQty, text=(valSearch+" currently stored:", quantity), font=("Helvetica", 15)).place(x=0,y=60)
            vegSearchEntry = Entry(windowQty, width=50, font=("Helvetica", 20)).place(x=0, y=120)
            button0=Button(windowQty, text="0").place(x=200, y=320)
            button1=Button(windowQty, text="1").place(x=160, y=200)
            button2=Button(windowQty, text="2").place(x=200, y=200)
            button3=Button(windowQty, text="3").place(x=240, y=200)
            button4=Button(windowQty, text="4").place(x=160, y=240)
            button5=Button(windowQty, text="5").place(x=200, y=240)
            button6=Button(windowQty, text="6").place(x=240, y=240)
            button7=Button(windowQty, text="7").place(x=160, y=280)
            button8=Button(windowQty, text="8").place(x=200, y=280)
            button9=Button(windowQty, text="9").place(x=240, y=280)
            fillBackBtn= Button(windowQty, text="Back", command=windowQty.destroy).place(x=0, y=450)
        #end of quantityWindow()
            
        cursor.execute("select * from vegetables where name=%s",valSearch)
        affectedRow = cursor.rowcount
        data = cursor.fetchall()
        if affectedRow == 0:
            itemNotFoundLbl=Label(windowFill,text=(valSearch+" is not present in database,\n would you like to add it?"),font=("Helvetica", 18)).place(x=20,y=150)
            addYesBtn=Button(windowFill, text="Yes", font=("Helvetica",15), bg="#75d179").place(x=100,y=220)
            addNoBtn=Button(windowFill, text="No", font=("Helvetica",15), bg= "red", fg="white").place(x=170,y=220)
        else:
            print(data)
       
            quantityWindow()
     #getNameFromDB ends here
            
    fillBackBtn= Button(windowFill, text="Back", command=windowFill.destroy).place(x=0, y=450)
    fillOkBtn= Button(windowFill, text="Ok", command=getNameFromDB).place(x=450, y=450)
    print("ok")

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

