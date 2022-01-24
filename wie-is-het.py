from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Wie is het (GUI Update)")
window.geometry("300x200")

antwoorden = ["Ja","Nee"]

def cheeseAnswer(name):
    question.destroy()
    previousQ.destroy()
    Combo.destroy()
    button.destroy()
    finalAnswer = tk.Label(text=name,font=("Calibri Light", 12))
    finalAnswer.pack(pady=60)

def buffer():
    answer = Combo.get()
    if answer == "Ja":
        cheeseHoles()
    elif answer == "Nee":
        cheeseBlue()
def bufferHoles():
    answer = Combo.get()
    if answer == "Ja":
        cheesePrice()
    elif answer == "Nee":
        cheeseHard()
def bufferPrice():
    answer = Combo.get()
    if answer == "Ja":
        cheeseAnswer("Emmenthaler")
    elif answer == "Nee":
        cheeseAnswer("Leerdammer")
def bufferHard():
    answer = Combo.get()
    if answer == "Ja":
        cheeseAnswer("Parmigano Reggiano")
    elif answer == "Nee":
        cheeseAnswer("Goudse kaas")
def cheeseHoles():
    question.configure(text="Zitten er gaten in?")
    question.place(y=50,x=90)
    previousQ.configure(text="Vorige vraag: Is de kaas geel?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferHoles)
def cheesePrice():
    question.configure(text="Is de kaas belachelijk duur? ")
    question.place(y=50,x=65)
    previousQ.configure(text="Vorige vraag: Zitten er gaten in?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferPrice)
def cheeseHard():
    question.configure(text="Is de kaas hard als steen?")
    question.place(y=50,x=65)
    previousQ.configure(text="Vorige vraag: Zitten er gaten in?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferHard)

def bufferBlue():
    answer = Combo.get()
    if answer == "Ja":
        cheeseBorder()
    elif answer == "Nee":
        cheeseBorder2()
def bufferBorder():
    answer = Combo.get()
    if answer == "Ja":
        cheeseAnswer("Bleu de Rochbaron")
    elif answer == "Nee":
        cheeseAnswer("Fourme d'Ambert")
def bufferBorder2():
    answer = Combo.get()
    if answer == "Ja":
        cheeseAnswer("Camembert")
    elif answer == "Nee":
        cheeseAnswer("Mozzarella")
def cheeseBlue():
    question.configure(text="Heeft de kaas blauwe schimmels? ")
    question.place(y=50,x=40)
    previousQ.configure(text="Vorige vraag: Is de kaas geel?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferBlue)
def cheeseBorder():
    question.configure(text="Heeft de kaas een korst? ")
    question.place(y=50,x=65)
    previousQ.configure(text="Vorige vraag: Heeft de kaas blauwe schimmels?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferBorder)
def cheeseBorder2():
    question.configure(text="Heeft de kaas een korst?")
    question.place(y=50,x=65)
    previousQ.configure(text="Vorige vraag: Heeft de kaas blauwe schimmels?")
    previousQ.pack()
    Combo.set("")
    button.configure(command=bufferBorder2)

previousQ = tk.Label( font=("Calibri Light", 10))
question = tk.Label(text="Is de kaas geel?", font=("Calibri Light", 12))
question.place(y=50,x=100)
Combo = ttk.Combobox(width=10,values=antwoorden, font=("Calibri Light", 12))
Combo.place(y=80, x=100)
button = tk.Button(bd=0.5,text="Antwoord verzenden", command=buffer) 
button.place(y=150, x=90)

window.mainloop()