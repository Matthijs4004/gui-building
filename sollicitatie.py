import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("sollicitatie (GUI Update)")
window.geometry("450x100")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

JaNee = ["Ja", "Nee"]
naamVar = tk.StringVar()
dressuurVar = tk.IntVar()
jonglerenVar = tk.IntVar()
acrobatiekVar = tk.IntVar()
lichaamslengteVar = tk.IntVar()
lichaamsgewichtVar = tk.IntVar()

# dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
# jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
# acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
# lichaamslengte = int(input("Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? "))
# lichaamsgewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
# diploma = input("Bent u in het bezit van een diploma MBO-4 ondernemen? Ja/Nee ")
# hogehoed = input("Bent u in het bezit van een hoge hoed? Ja/Nee ")
# rijbewijs = input("Bent u in het bezit van een geldig vrachtwagen rijbewijs? Ja/Nee ")
# certificaat = input("Bent u in het bezit van het Certificaat “Overleven met gevaarlijk personeel”? Ja/Nee ")
# geslacht = input("Welke geslacht bent u? (man/vrouw) ")

def Start():
    global vraagLabel, vraagInput, button
    vraagLabel = tk.Label(text="Sollicitatie formulier Circus directeur",font=("Calibri Light", 11))
    vraagLabel.place(y=5,x=110)
    vraagInput = tk.Entry(width=30,font=("Calibri Light", 11))
    button = tk.Button(text="Volgende",bd=0.5, command=naam)
    button.place(y=60,x=190)

def naam():
    vraagLabel.configure(text="Wat is uw naam?")
    vraagLabel.place(y=5,x=160)
    vraagInput.configure(textvariable=naamVar)
    vraagInput.place(y=30,x=100)
    button.configure(command=dressuur)

def dressuur():
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=dressuurVar)
    button.configure(command=jongleren)

def jongleren():
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met jongleren?")
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=jonglerenVar)
    button.configure(command=acrobatiek)

def acrobatiek():
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met acrobatiek?")
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=acrobatiekVar)
    button.configure(command=lichaamslengte)

def lichaamslengte():
    vraagLabel.configure(text="Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? ")
    vraagLabel.place(y=5,x=20)
    vraagInput.configure(textvariable=lichaamslengteVar)
    button.configure(command=lichaamsgewicht)

def lichaamsgewicht():
    vraagLabel.configure(text="Wat is uw lichaamsgewicht in hele kg? ")
    vraagLabel.place(y=5,x=110)
    vraagInput.configure(textvariable=lichaamsgewichtVar)
    button.configure(command=diploma)

def diploma():
    vraagLabel.configure(text="Bent u in het bezit van een diploma MBO-4 ondernemen?")
    vraagLabel.place(y=5,x=50)
    vraagInput.destroy()
    vraagInput2 = ttk.Combobox(width=30,values=JaNee)
    vraagInput2.place(y=30,x=120)
    button.configure(command=hogehoed)

def hogehoed():
    pass


Start()
window.mainloop()



