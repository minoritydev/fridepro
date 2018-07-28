from tkinter import *


windowQty=Tk()
vegSearchEntry = Entry(windowQty, width=50, font=("Helvetica", 20))
vegSearchEntry.place(x=0, y=120)


def numpadInput(num):
    global pos   # this will make sure that the increment following next line is on the variable that is outside the numpadInput() function 
                 # If this does not work in our ui.py file , try putting the line #16 in the most outside scope in ui.py
    
    vegSearchEntry.insert(pos,num)           
    pos+=1

pos=0
button0=Button(windowQty, text="0",command=lambda:numpadInput("0")).place(x=200, y=320)
button1=Button(windowQty, text="1",command=lambda:numpadInput("1")).place(x=160, y=200)
button2=Button(windowQty, text="2",command=lambda:numpadInput("2")).place(x=200, y=200)
button3=Button(windowQty, text="3",command=lambda:numpadInput("3")).place(x=240, y=200)
button4=Button(windowQty, text="4",command=lambda:numpadInput("4")).place(x=160, y=240)
button5=Button(windowQty, text="5",command=lambda:numpadInput("5")).place(x=200, y=240)
button6=Button(windowQty, text="6",command=lambda:numpadInput("6")).place(x=240, y=240)
button7=Button(windowQty, text="7",command=lambda:numpadInput("7")).place(x=160, y=280)
button8=Button(windowQty, text="8",command=lambda:numpadInput("8")).place(x=200, y=280)
button9=Button(windowQty, text="9",command=lambda:numpadInput("9")).place(x=240, y=280)

windowQty.mainloop()


