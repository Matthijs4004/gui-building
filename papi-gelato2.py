import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

window = tk.Tk()
window.geometry("300x300")
window.title("Papi Gelato (GUI Update)")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

Smaken = ["A","C","V"]
AB = ["A","B"]
Toppings = ["A","B","C","D"]
EenTwee = ["1", "2"]
JaNee = ["Ja","Nee"]
alBakje = False
literNum = 1
bolNum = 1
alleToppings = 0
aantalBolletjes = 0
aantalHoorntjes = 0
aantalBakjes = 0
aantalSlagroom = 0
aantalSprinkels = 0
aantalCaramel = 0
topping = 0
slagroomPrijs = 0.50
sprinkelsPrijs = 0.30
caramelHoorntje = 0.60
caramelBakje = 0.90
bolletjePrijs = 0.95
hoorntjePrijs = 0.70
bakjePrijs = 0.50
getallen = list(range(0,1000))
marktInput = tk.IntVar()
literInput = tk.IntVar()
bolInput = tk.IntVar()
smaakLInput = tk.StringVar()
smaakBInput = tk.StringVar()
toppingInput = tk.StringVar()
houderInput = tk.StringVar()
nogmaalsInput = tk.StringVar()
houder = tk.StringVar()


def showError():
    showerror("Vul iets in", "Vul een getal hoger dan 0 in!")
def showErrorS():
    showerror("Error", "Sorry, dat snap ik niet...")
def showErrorB():
    showerror("Error",'Sorry, zulke grote bakken hebben we niet')

def destroyWidgets():
    questionInput.destroy()
    question.destroy()
    button.destroy()


def keuze():
    welkom.configure(text="Welkom bij Papi Gelato!",font=("Calibri Light", 20))
    welkom.place(y=5,x=15)
    question.configure(text="Bent u 1) particulier of 2) zakelijk?",font=("Calibri Light", 13))
    question.place(y=120,x=30)
    questionInput.configure(width=10,values=EenTwee,textvariable=marktInput)
    questionInput.place(y=150,x=105)
    button.configure(width=11,bd=0.5,text="Volgende",command=keuze)
    button.place(y=250,x=105)
    markt = marktInput.get()
    if markt == 1:
        particulier()
    elif markt == 2:
        zakelijk()
    elif markt == 0:
        print("Leeg")
    else:
        print("Error")
        #showError()
        #keuze()

def zakelijk():
    questionInput.configure(values=getallen,textvariable=literInput)
    question.configure(text="Hoeveel liter ijs wilt u? ")
    question.place(y=120,x=70)
    button.configure(command=zakelijkLiterCheck)

def zakelijkLiterCheck():
    liter = literInput.get()
    if liter >= 1:
        print("Zakelijke Smaak")
        zakelijk2()
    else:
        showError()

def zakelijk2():
    global literNum
    question.configure(text="Welke smaak wilt u voor liter nummer "+ str(literNum) +"?\nA) Aardbei, C) Chocolade of V) Vanille ")
    questionInput.configure(values=Smaken,textvariable=smaakLInput)
    button.configure(command=zakelijkSmaakCheck)
    literNum += 1
    question.place(y=100,x=10)

def zakelijkSmaakCheck():
    smaakL = smaakLInput.get()
    liter = literInput.get()
    if smaakL == "A" or smaakL == "C" or smaakL == "V":
        zakelijk2()
    if literNum == (liter + 1):
        zakelijkeBon()

def zakelijkeBon():
    liter = literInput.get()
    literPrijs = liter * 9.80
    quotient = literPrijs / 100
    procent = quotient*6
    destroyWidgets()
    bon1 = tk.Label(text="--------------[Papi Gelato]--------------\n",font=("Calibri Light", 12))
    bon2 = tk.Label(text=(f"Liter         {liter} x € 9.80 = €{round(literPrijs, 3)}"),font=("Calibri Light", 12))
    bon3 = tk.Label(text='                                     ----- +',font=("Calibri Light", 12))
    bon4 = tk.Label(text=(f"Totaal                          €{round(literPrijs,3)}"),font=("Calibri Light", 12))
    bon5 = tk.Label(text=(f"BTW (6%)                     €{round(procent, 2)}"),font=("Calibri Light", 12))
    bon1.place(y=50,x=35)
    bon2.place(y=70,x=35)
    bon3.place(y=90,x=35)
    bon4.place(y=110,x=35)
    bon5.place(y=130,x=35)

def particulier():
    questionInput.configure(values=getallen,textvariable=bolInput)
    question.configure(text="Hoeveel bolletjes wilt u? ")
    question.place(y=120,x=60)
    button.configure(command=particulierBolCheck)

def particulierBolCheck():
    global aantalBakjes, alBakje, aantalBolletjes
    bol = bolInput.get()
    if bol in range(1,4):
        aantalBolletjes += bol
        particulier2()
    elif bol in range(4,8):
        aantalBakjes += 1
        aantalBolletjes += bol
        alBakje = True
        houder.set("bakje")
        particulier2()
    elif bol >= 8:
        showErrorB()
    else:
        showErrorS()

def particulier2():
    global bolNum
    question.configure(text="Welke smaak wilt u voor bol nummer "+ str(bolNum) +"?\nA) Aardbei, C) Chocolade of V) Vanille ")
    questionInput.configure(values=Smaken,textvariable=smaakBInput)
    button.configure(command=particulierSmaakCheck)
    bolNum += 1
    question.place(y=100,x=10)

def particulierSmaakCheck():
    smaakB = smaakBInput.get()
    bol = bolInput.get()
    if smaakB == "A" or smaakB == "C" or smaakB == "V":
        particulier2()
    if bolNum == (bol + 2):
        if alBakje == True:
            particulier4()
        else:
            particulier3()

def particulier3():
    question.configure(text="Wilt u deze "+ str(bolInput.get()) +" bolletje(s) in \nA) een hoorntje of B) een bakje? ")
    questionInput.configure(values=AB,textvariable=houderInput)
    button.configure(command=bakjeOfhoorntje)
    question.place(y=100,x=35)

def bakjeOfhoorntje():
    global houder, aantalHoorntjes, aantalBakjes
    h = houderInput.get()
    if h == "A":
        houder.set("hoorntje")
        aantalHoorntjes += 1
        particulier4()
    elif h == "B":
        houder.set("bakje")
        aantalBakjes += 1
        particulier4()
    else:
        showErrorS()

def particulier4():
    question.configure(text="Wat voor topping wilt u: A) Geen, \nB) Slagroom, C) Sprinkels of D) Caramel Saus?",font=("Calibri Light", 11))
    question.place(y=100,x=20)
    questionInput.configure(values=Toppings,textvariable=toppingInput)
    button.configure(command=toppingsCheck)

def toppingsCheck(): # toppings
    global topping, aantalSlagroom, aantalSprinkels, aantalCaramel
    top = toppingInput.get()
    if top == "A":
        particulier5()
    elif top == "B":
        aantalSlagroom += slagroomPrijs
        topping =+ 1
        particulier5()
    elif top == "C":
        aantalSprinkels += sprinkelsPrijs * aantalBolletjes
        topping =+ 1
        particulier5()
    elif top == "D":
        if houder.get() == "hoorntje":
            aantalCaramel += caramelHoorntje
        if houder.get() == "bakje":
            aantalCaramel += caramelBakje
        topping =+ 1
        particulier5()
    else:
        showError()

def particulier5():
    question.configure(text="Hier is uw "+str(houder.get())+" met "+str(bolInput.get())+" bolletje(s). \nWilt u nog meer bestellen? Y/N ",font=("Calibri Light", 12))
    question.place(y=100,x=40)
    questionInput.configure(values=JaNee,textvariable=nogmaalsInput)
    button.configure(command=nogmaalsCheck)

def nogmaalsCheck():
    global bolNum
    nogmaals = nogmaalsInput.get()
    if nogmaals == "Ja":
        bolNum = 1
        keuze()
    elif nogmaals == "Nee":
        bon()
        print("Bedankt en tot ziens!")
    else:
        showErrorS()

def bon():
    global alleToppings
    totaalBol = aantalBolletjes * bolletjePrijs
    totaalHoorntje = aantalHoorntjes * hoorntjePrijs
    totaalBak = aantalBakjes * bakjePrijs
    totaalTopping = aantalSlagroom + aantalCaramel + aantalSprinkels
    totaalBedrag = totaalBol + totaalHoorntje + totaalBak + totaalTopping
    alleToppings += topping
    destroyWidgets()
    bon1 = tk.Label(text="--------------[Papi Gelato]--------------\n",font=("Calibri Light", 12))
    bon1.place(y=50,x=35)
    if aantalBolletjes >= 1:
        bon2 = tk.Label(text=(f"Bolletje(s)   {aantalBolletjes} x €0.95 = €{round(totaalBol, 2)}"),font=("Calibri Light", 12))
        bon2.place(y=70,x=35)
    if aantalHoorntjes >= 1:
        bon3 = tk.Label(text=(f"Hoorntje(s)  {aantalHoorntjes} x €0.70 = €{round(totaalHoorntje, 2)}"),font=("Calibri Light", 12))
        bon3.place(y=90,x=35)
    if aantalBakjes >= 1:
        bon4 = tk.Label(text=(f"Bakje(s)      {aantalBakjes} x €0.50 = €{round(totaalBak, 2)}"),font=("Calibri Light", 12))
        bon4.place(y=110,x=35)
    if topping >= 1:
        bon4 = tk.Label(text=(f"Topping(s)   {alleToppings} x €{round(totaalTopping, 2)} = €{round(totaalTopping, 2)}"),font=("Calibri Light", 12))
        bon4.place(y=130,x=35)
    bon3 = tk.Label(text='                                     ----- +',font=("Calibri Light", 12))
    bon3.place(y=150,x=35)
    bon4 = tk.Label(text=(f"Totaal                          €{round(totaalBedrag, 2)}"),font=("Calibri Light", 12))
    bon4.place(y=180,x=35)

welkom = tk.Label(text="Welkom bij Papi Gelato!",font=("Calibri Light", 20))
welkom.place(y=5,x=15)
question = tk.Label(text="Bent u 1) particulier of 2) zakelijk?",font=("Calibri Light", 13))
question.place(y=120,x=30)
questionInput = ttk.Combobox(width=10,values=EenTwee,textvariable=marktInput)
questionInput.place(y=150,x=105)
button = tk.Button(width=11,bd=0.5,text="Volgende",command=keuze)
button.place(y=250,x=105)
#particulier4()
window.mainloop()