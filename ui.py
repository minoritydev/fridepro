from tkinter import *
window = Tk()
frame = Frame(window).place(x=250,y=250)
#fucntions
def onClickFill():
    
    self.frame.destroy()
    fillFrame = Frame(window)
    
    window.title("Welcome to LikeGeeks app")
   
    vegSearchLabel = Label(fillFrame, text="Please enter name of product:", font=("Helvetica", 22)).place(x=0,y=0)
    vegSearchEntry = Entry(fillFrame, width=50).place(x=0, y=60)
#function over
    
#main window
window.geometry("500x500")
window.title("Welcome to LikeGeeks app")
fillBtn = Button(frame, text="FILL", height=17, width=60, bg="#75d179", command=onClickFill).place(x=0, y=0)
takeBtn = Button(frame, text="TAKE", height=17, width=60, bg="blue").place(x=0,y=250)
#main window over



window.mainloop()
