import tkinter
from tkinter import ttk
from tkinter.constants import SUNKEN






window=tkinter.Tk()
window.title('aycalculator')


frame=tkinter.Frame(master=window, bg="yellow", padx=50, pady=50)


frame.grid()
ttk.Label(frame, text="calculator").grid(column=0,row=0)
entry=ttk.Entry(frame)
entry.grid(row=10, column=0, columnspan=500, ipady=2, pady=2, padx=70, ipadx=70)
ttk.Button(frame, text="AC")
ttk.Button(frame, text="+/-").grid(column=25, row =50)
ttk.Button(frame, text="%").grid(column=35,row=50)
ttk.Button(frame, text="÷", command=lambda:handleclick("÷")).grid(column=40,row=50)
ttk.Button(frame, text="7", command=lambda:handleclick(7)).grid(column=15,row=60)
ttk.Button(frame, text="8", command=lambda:handleclick(8)).grid(column=25,row=60)
ttk.Button(frame, text="9", command=lambda:handleclick(9)).grid(column=35,row=60)
ttk.Button(frame, text="x", command=lambda:handleclick("*")).grid(column=40,row=60)
ttk.Button(frame, text="4", command=lambda:handleclick(4)).grid(column=15,row=70)
ttk.Button(frame, text="5", command=lambda:handleclick(5)).grid(column=25,row=70)
ttk.Button(frame, text="6", command=lambda:handleclick(6)).grid(column=35,row=70)
ttk.Button(frame, text="-", command=lambda:handleclick("-")).grid(column=40,row=70)
ttk.Button(frame, text="1", command=lambda:handleclick(1)).grid(column=15,row=80)
ttk.Button(frame, text="2", command=lambda:handleclick(2)).grid(column=25,row=80)
ttk.Button(frame, text="3", command=lambda:handleclick(3)).grid(column=35,row=80)
ttk.Button(frame, text="+", command=lambda:handleclick("+")).grid(column=40,row=80)
ttk.Button(frame, text="0", command=lambda:handleclick(0)).grid(column=15, row=90)
ttk.Button(frame, text=".").grid(column=35,row=90)
ttk.Button(frame, text="=").grid(column=40,row=90)


def handleclick(num):
   entry.insert(tkinter.END,num)

frame.pack()
window.mainloop()



