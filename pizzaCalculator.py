from cProfile import label
from cgitb import text
from distutils import command
import glob
import tkinter as tk

window = tk.Tk()
window.title("Pizza Calculator (GUI Update)")
window.geometry("300x200")

largeQty = tk.StringVar()
mediumQty = tk.StringVar()
smallQty = tk.StringVar()

largePrice = tk.Label(text="Large Pizza: €12,-",font=("Calibri Light", 12))
largePrice.pack(padx=5)
mediumPrice = tk.Label(text="Medium Pizza: €7,-",font=("Calibri Light", 12))
mediumPrice.pack(padx=5)
smallPrice = tk.Label(text="Small Pizza: €4,-",font=("Calibri Light", 12))
smallPrice.pack(padx=5)

def largePizza():
    global largeLabel, largeEntry
    largeLabel = tk.Label(text="Hoeveel large Pizza's wilt u bestellen?",font=("Calibri Light", 11))
    largeLabel.place(y=100,x=40)
    largeEntry = tk.Entry(width=10, textvariable=largeQty)
    largeEntry.place(y=130,x=120)
    button.configure(command=mediumPizza)
def mediumPizza():
    global mediumEntry, mediumLabel
    largeLabel.destroy()
    largeEntry.destroy()
    mediumLabel = tk.Label(text="Hoeveel medium Pizza's wilt u bestellen?",font=("Calibri Light", 11))
    mediumLabel.place(y=100,x=40)
    mediumEntry = tk.Entry(width=10, textvariable=mediumQty)
    mediumEntry.place(y=130,x=120)
    button.configure(command=smallPizza)
def smallPizza():
    global smallEntry, smallLabel
    mediumLabel.destroy()
    mediumEntry.destroy()
    smallLabel = tk.Label(text="Hoeveel small Pizza's wilt u bestellen?",font=("Calibri Light", 11))
    smallLabel.place(y=100,x=40)
    smallEntry = tk.Entry(width=10, textvariable=smallQty)
    smallEntry.place(y=130,x=120)
    button.configure(command=pizzaAmount)

def pizzaAmount():
    global largeAmount, mediumAmount, smallAmount
    smallLabel.destroy()
    smallEntry.destroy()
    largeAmount = tk.Label(text="Hoeveelheid large Pizza's: " + largeQty.get(),font=("Calibri Light", 11))
    largeAmount.place(y=90,x=40)
    mediumAmount = tk.Label(text="Hoeveelheid medium Pizza's: " + mediumQty.get(),font=("Calibri Light", 11))
    mediumAmount.place(y=110,x=40)
    smallAmount = tk.Label(text="Hoeveelheid small Pizza's: " + smallQty.get(),font=("Calibri Light", 11))
    smallAmount.place(y=130,x=40)
    button.configure(text="Bereken Prijs", command=prijsBerekenen)

def prijsBerekenen():
    largeAmount.destroy()
    mediumAmount.destroy()
    smallAmount.destroy()
    button.destroy()
    large = largeQty.get()
    medium = mediumQty.get()
    small = smallQty.get()
    largeTotaal = int(large) * 12
    mediumTotaal = int(medium) * 7
    smallTotaal = int(small) * 4
    TotaalBedrag = largeTotaal + mediumTotaal + smallTotaal
    TotaalLabel = tk.Label(text="Het totaalbedrag is: " + str(TotaalBedrag),font=("Calibri Light", 12))
    TotaalLabel.place(y=100,x=40)


button = tk.Button(text="Volgende", command=largePizza)
button.place(y=160,x=120)

largePizza()
window.mainloop()