from distutils import ccompiler
from glob import glob
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Sollicitatie (GUI Update)")
window.geometry("450x100")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

JaNee = ["Ja", "Nee"]
ManVrouw = ["Man", "Vrouw"]
naamVar = tk.StringVar()
dressuurVar = tk.IntVar()
jonglerenVar = tk.IntVar()
acrobatiekVar = tk.IntVar()
lichaamslengteVar = tk.IntVar()
lichaamsgewichtVar = tk.IntVar()
diplomaVar = tk.StringVar()
hogehoedVar = tk.StringVar()
rijbewijsVar = tk.StringVar()
certificaatVar = tk.StringVar()
geslachtVar = tk.StringVar()
snorVar = tk.StringVar()
snorBVar = tk.StringVar()
haarVar = tk.StringVar()
haarLVar = tk.StringVar()

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
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?") # > 4
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=dressuurVar)
    button.configure(command=jongleren)

def jongleren():
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met jongleren?") # > 5
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=jonglerenVar)
    button.configure(command=acrobatiek)

def acrobatiek():
    vraagLabel.configure(text="Hoeveel jaar praktijkervaring heeft u met acrobatiek?") # > 3
    vraagLabel.place(y=5,x=50)
    vraagInput.configure(textvariable=acrobatiekVar)
    button.configure(command=lichaamslengte)

def lichaamslengte():
    vraagLabel.configure(text="Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? ") # > 150
    vraagLabel.place(y=5,x=20)
    vraagInput.configure(textvariable=lichaamslengteVar)
    button.configure(command=lichaamsgewicht)

def lichaamsgewicht():
    vraagLabel.configure(text="Wat is uw lichaamsgewicht in hele kg? ") # > 90
    vraagLabel.place(y=5,x=110)
    vraagInput.configure(textvariable=lichaamsgewichtVar)
    button.configure(command=diploma)

def diploma():
    global vraagInput2
    vraagLabel.configure(text="Bent u in het bezit van een diploma MBO-4 ondernemen?") # ja
    vraagLabel.place(y=5,x=50)
    vraagInput.destroy()
    vraagInput2 = ttk.Combobox(width=30,values=JaNee, textvariable=diplomaVar)
    vraagInput2.place(y=30,x=120)
    button.configure(command=hogehoed)

def hogehoed():
    vraagLabel.configure(text="Bent u in het bezit van een hoge hoed?") # ja
    vraagLabel.place(y=5,x=110)
    vraagInput2.configure(textvariable=hogehoedVar)
    button.configure(command=rijbewijs)
    
def rijbewijs():
    vraagLabel.configure(text="Bent u in het bezit van een geldig vrachtwagen rijbewijs?") # ja
    vraagLabel.place(y=5,x=45)
    vraagInput2.configure(textvariable=rijbewijsVar)
    button.configure(command=certificaat)

def certificaat():
    vraagLabel.configure(text="Bent u in het bezit van het Certificaat “Overleven met gevaarlijk personeel”?") # ja
    vraagLabel.place(y=5,x=5)
    vraagInput2.configure(textvariable=certificaatVar)
    button.configure(command=geslacht)

def geslacht():
    vraagLabel.configure(text="Welke geslacht bent u?") # Man / Vrouw
    vraagLabel.place(y=5,x=150)
    vraagInput2.configure(textvariable=geslachtVar, values=ManVrouw)
    button.configure(command=geslachtCheck)

def geslachtCheck():
    if geslachtVar.get() == "Man":
        snor()
    else:
        haar()

def snor():
    vraagLabel.configure(text="Heeft u een snor?") # Ja
    vraagLabel.place(y=5,x=160)
    vraagInput2.configure(textvariable=snorVar, values=JaNee)
    button.configure(command=snorB)

def snorB():
    vraagLabel.configure(text="Is uw snor breder dan 10cm?") # Ja
    vraagLabel.place(y=5,x=140)
    vraagInput2.configure(textvariable=snorBVar, values=JaNee)
    button.configure(command=eind)

def haar():
    vraagLabel.configure(text="Draagt u rood krulhaar?") # Ja
    vraagLabel.place(y=5,x=150)
    vraagInput2.configure(textvariable=haarVar, values=JaNee)
    button.configure(command=haarL)

def haarL():
    vraagLabel.configure(text="Is uw rood krulhaar langer dan 20cm?") # Ja
    vraagLabel.place(y=5,x=150)
    vraagInput2.configure(textvariable=haarLVar, values=JaNee)
    button.configure(command=eind, text="Einde")

def eind():
    if dressuurVar.get() > 4 or jonglerenVar.get() > 5 or acrobatiekVar.get() > 3 and lichaamslengteVar.get() > 150 and lichaamsgewichtVar.get() > 90 and diplomaVar.get()== "Ja" and hogehoedVar.get() == "Ja" and rijbewijsVar.get() == "Ja" and certificaatVar.get() == "Ja" and snorVar.get() == "Ja" or haarVar.get() and snorBVar.get() == "Ja" or haarLVar.get() == "Ja":
        button.destroy()
        vraagInput2.destroy()
        vraagLabel.configure(text="Proficiat! U komt in aanmerking voor een sollicitatiegesprek.")
        vraagLabel.place(y=5,x=45)
    else:
        button.destroy()
        vraagInput2.destroy()
        vraagLabel.configure(text="U voldoet niet aan onze strenge eisen voor de functie van Circus directeur")
        vraagLabel.place(y=5,x=5)

Start()
window.mainloop()