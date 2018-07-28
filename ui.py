from tkinter import *
import pymysql
#database
db =  pymysql.connect(
    host='localhost',
    user='root',
    passwd='1337',
    db='fridepro'
)
db.autocommit(True)
cursor=db.cursor()
pos=0
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
            vegQtyEntry = Entry(windowQty, width=50, font=("Helvetica", 20))
            vegQtyEntry.place(x=0, y=120)
##            
##            def buttonInput(num):
##                vegQtyEntry.insert(1, num)
##                return
            def numpadInput(num):
                global pos  # this will make sure that the increment following next line is on the variable that is outside the numpadInput() function 
                             # put this function in quantityWindow() and line # 17 inside the block of quantityWindow() 
                             # If this does not work in our ui.py file , try putting the line #17 of this file in the most outside scope in ui.py (preferrably below import lines)
                
                vegQtyEntry.insert(pos,num)           
                pos+=1

            

            def addToDB():
                qtyToAdd = vegQtyEntry.get()
                qtyToAddInt = int(qtyToAdd)
                
                cursor.execute("update vegetables set quantity=quantity + %s where name = %s", (qtyToAddInt,valSearch))
                windowQty.destroy()
                windowFillDone = Tk()
                windowFillDone.title("Fill Successfull")
                windowFillDone.geometry("500x500")
                fillDoneLabel = Label(windowFillDone, text=(qtyToAdd+" of "+valSearch+" has been added!"), font=("Helvetica", 22)).place(x=50,y=200)
                fillDoneBtn = Button(windowFillDone, text = "OK", font=("Helvetica", 20), command=windowFillDone.destroy).place(x=250, y=250)
                
            button0=Button(windowQty, bg="#4286f4",text="0",command=lambda:numpadInput("0")).place(x=200, y=320)
            button1=Button(windowQty, text="1",command=lambda:numpadInput("1")).place(x=160, y=200)
            button2=Button(windowQty, text="2",command=lambda:numpadInput("2")).place(x=200, y=200)
            button3=Button(windowQty, text="3",command=lambda:numpadInput("3")).place(x=240, y=200)
            button4=Button(windowQty, bg="#4286f4", text="4",command=lambda:numpadInput("4")).place(x=160, y=240)
            button5=Button(windowQty, bg="#4286f4",text="5",command=lambda:numpadInput("5")).place(x=200, y=240)
            button6=Button(windowQty, bg="#4286f4",text="6",command=lambda:numpadInput("6")).place(x=240, y=240)
            button7=Button(windowQty, text="7",command=lambda:numpadInput("7")).place(x=160, y=280)
            button8=Button(windowQty, text="8",command=lambda:numpadInput("8")).place(x=200, y=280)
            button9=Button(windowQty, text="9",command=lambda:numpadInput("9")).place(x=240, y=280)
            fillBackBtn= Button(windowQty, text="Back", command=windowQty.destroy).place(x=0, y=450)
            fillOkBtn= Button(windowQty, text="Ok", command=addToDB).place(x=450, y=450)
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
            windowFill.destroy()
     #getNameFromDB ends here
            
    fillBackBtn= Button(windowFill, text="Back", command=windowFill.destroy).place(x=0, y=450)
    fillOkBtn= Button(windowFill, text="Ok", command=getNameFromDB).place(x=450, y=450)
    print("ok")

def onClickTake():
    def getNameFromDBTake():
        valSearch=vegSearchEntry.get()
    
        def quantityTakeWindow(): #opens new window to enter quantity of item
                cursor.execute("select quantity from vegetables where name=%s",valSearch)
                quantity = cursor.fetchall()
                windowTakeQty= Tk()
                windowTakeQty.title("Enter Amount to Take")
                windowTakeQty.geometry("500x500")
                vegQtyInputLabel = Label(windowTakeQty, text=("How many "+valSearch+" will you take out?"), font=("Helvetica", 22)).place(x=0,y=0)
                vegPresentQtyLabel = Label(windowTakeQty, text=(valSearch+" currently stored:", quantity), font=("Helvetica", 15)).place(x=0,y=60)
                vegQtyEntry = Entry(windowTakeQty, width=50, font=("Helvetica", 20))
                vegQtyEntry.place(x=0, y=120)
    ##            
    ##            def buttonInput(num):
    ##                vegQtyEntry.insert(1, num)
    ##                return
                
                def numpadInput(num):
                    global pos  # this will make sure that the increment following next line is on the variable that is outside the numpadInput() function 
                                 # put this function in quantityWindow() and line # 17 inside the block of quantityWindow() 
                                 # If this does not work in our ui.py file , try putting the line #17 of this file in the most outside scope in ui.py (preferrably below import lines)
                    
                    vegQtyEntry.insert(pos,num)           
                    pos+=1    

                def takeFromDB():
                    qtyToAdd = vegQtyEntry.get()
                    qtyToAddInt = int(qtyToAdd)
                    
                    cursor.execute("update vegetables set quantity=quantity - %s where name = %s", (qtyToAddInt,valSearch))
                    windowTakeQty.destroy()
                    windowTakeDone = Tk()
                    windowTakeDone.title("Fill Successfull")
                    windowTakeDone.geometry("500x500")
                    takeDoneLabel = Label(windowTakeDone, text=(qtyToAdd+" of "+valSearch+" is removed!"), font=("Helvetica", 22)).place(x=50,y=200)
                    takeDoneBtn = Button(windowTakeDone, text = "OK", font=("Helvetica", 20), command=windowTakeDone.destroy).place(x=250, y=250)
                    
                button0=Button(windowTakeQty, bg="#4286f4",text="0",command=lambda:numpadInput("0")).place(x=200, y=320)
                button1=Button(windowTakeQty, text="1",command=lambda:numpadInput("1")).place(x=160, y=200)
                button2=Button(windowTakeQty, text="2",command=lambda:numpadInput("2")).place(x=200, y=200)
                button3=Button(windowTakeQty, text="3",command=lambda:numpadInput("3")).place(x=240, y=200)
                button4=Button(windowTakeQty, bg="#4286f4",text="4",command=lambda:numpadInput("4")).place(x=160, y=240)
                button5=Button(windowTakeQty, bg="#4286f4",text="5",command=lambda:numpadInput("5")).place(x=200, y=240)
                button6=Button(windowTakeQty, bg="#4286f4",text="6",command=lambda:numpadInput("6")).place(x=240, y=240)
                button7=Button(windowTakeQty, text="7",command=lambda:numpadInput("7")).place(x=160, y=280)
                button8=Button(windowTakeQty, text="8",command=lambda:numpadInput("8")).place(x=200, y=280)
                button9=Button(windowTakeQty, text="9",command=lambda:numpadInput("9")).place(x=240, y=280)
                fillBackBtn= Button(windowTakeQty, text="Back", command=windowTakeQty.destroy).place(x=0, y=450)
                fillOkBtn= Button(windowTakeQty, text="Ok", command=takeFromDB).place(x=450, y=450)
        
        cursor.execute("select * from vegetables where name=%s",valSearch)
        affectedRow = cursor.rowcount
        data = cursor.fetchall()
        if affectedRow == 0:
            itemNotFoundLbl=Label(windowTake,text=(valSearch+" is not present in database,\n would you like to add it?"),font=("Helvetica", 18)).place(x=20,y=150)
            addYesBtn=Button(windowTake, text="Yes", font=("Helvetica",15), bg="#75d179").place(x=100,y=220)
            addNoBtn=Button(windowTake, text="No", font=("Helvetica",15), bg= "red", fg="white").place(x=170,y=220)
        else:
            print(data)
       
            quantityTakeWindow()
            windowTake.destroy()    
    windowTake= Tk()
    windowTake.title("Take")
    windowTake.geometry("500x500")
    vegSearchLabel = Label(windowTake, text="What are item(s) are you taking out?", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(windowTake, width=50, font=("Helvetica", 20))
    vegSearchEntry.place(x=0, y=60)
    takeBackBtn= Button(windowTake, text="Back", command=windowTake.destroy).place(x=0, y=450)
    takeOkBtn= Button(windowTake, text="Ok", command=getNameFromDBTake).place(x=450, y=450)
def onClickView():
    cursor.execute("select name from vegetables")
    allItems = cursor.fetchall()
    print(allItems)
    windowView = Tk()
    windowView.geometry("500x500")
    windowView.title("Stored Items")
    nameLabel=Label(windowView, text=allItems).place(x=0,y=0)
#main window
window.geometry("500x500")
window.title("Main Window")
fillLbl = Label(window,text="Are you -", font=("Helvetica",10)).place(x=0,y=0)
fillBtn = Button(window, text="Filling in?", height=15, width=60, bg="#75d179", command=onClickFill,).place(x=0, y=20)
takeBtn = Button(window, text="Taking out?", height=17, width=60, bg="red", fg="white", command=onClickTake).place(x=0,y=250)
viewBtn = Button(window, text="See what is stored", height=3, width=60, bg="blue", fg="white", command=onClickView).place(x=0,y=230)

#main window over


window.mainloop()

