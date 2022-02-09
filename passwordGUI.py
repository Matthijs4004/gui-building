import string, random
import tkinter as tk

window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

passwordLength = tk.IntVar()
Password = tk.StringVar()

def generatePassword():
    myPassword = []
    password = []
    password += string.ascii_lowercase
    password += string.ascii_uppercase
    password += [1,2,3,4,5,6,7,8,9]
    #password += ["!","@","#","$","%","^","&","*"]

    myPassword += random.choices(password, k=passwordLength.get())
    Password.set(myPassword)

title = tk.Label(text="Password Generator", font=("Calibri Light", 20))
title.place(y=5,x=40)
lengthLabel = tk.Label(text="Password length: ", font=("Calibri Light", 13))
lengthLabel.place(y=60,x=20)
lengthEntry = tk.Entry(width=15, textvariable=passwordLength, font=("Calibri Light", 10))
lengthEntry.place(y=65,x=160)
passwordEntry = tk.Entry(width=40,textvariable=Password,font=("Calibri Light", 10))
passwordEntry.place(y=110,x=6)

button = tk.Button(bd=0.5,command=generatePassword,text="Generate Password", font=("Calibri Light", 10))
button.place(y=150,x=95)

window.mainloop()