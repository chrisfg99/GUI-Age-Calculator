#Christopher Greer
#GUI age calculator
#02/01/2023

#import Libaries   
from tkinter import *
from datetime import date

#intialise tkinter window
root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.title('Age Calculator')
ageOut = Label(root)

#initialise labels
l1 = Label(text="Name: ")
l1.grid(row=1, column=0)

l2 = Label(text="Year: ")
l2.grid(row=2, column=0)

l3 = Label(text="Month: ")
l3.grid(row=3, column=0)

l4 = Label(text="Date: ")
l4.grid(row=4, column=0)

#initialise inputs
nameValue=StringVar()
nameEntry = Entry(root, textvariable=nameValue)
nameEntry.grid(row=1, column=1, padx=10, pady=10)

yearValue=StringVar()
yearEntry = Entry(root, textvariable=yearValue)
yearEntry.grid(row=2, column=1, padx=10, pady=10)

monthValue=StringVar()
monthEntry = Entry(root, textvariable=monthValue)
monthEntry.grid(row=3, column=1, padx=10, pady=10)

dateValue=StringVar()
dayEntry = Entry(root, textvariable=dateValue)
dayEntry.grid(row=4, column=1, padx=10, pady=10)

#verification function
def verify():
    try:
        int(yearEntry.get())
        int(monthEntry.get())
        int(dayEntry.get())
    except ValueError:
        global ageOut
        ageOut.destroy()
        ageOut = Label(text="Please enter numbers for year, month and day fields.")
        ageOut.grid(row=6, column=1)
        

#age calculation function
def ageCalc():
    #verification on string
    verify()
    #get todays date
    today = date.today()
    #create birth date as date object
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age = today.year-birthDate.year
    if((today.month<birthDate.month) or (today.month == birthDate.month and 
    today.day<birthDate.day)):
        age=age-1
    #display age
    global ageOut
    ageOut.destroy()
    ageOut = Label(text=f"{nameValue.get()}'s age is {age}.")
    ageOut.grid(row=6, column=1)

#initialise button
b = Button(text="Calculate your age", command=ageCalc)
b.grid(row=5, column=1)

#run program in loop
root.mainloop()