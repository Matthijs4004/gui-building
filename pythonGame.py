import tkinter as tk
from tkinter import font, ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Adventure Game GUI Update")
window.geometry("650x250")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)]

bijlInput = tk.StringVar()
slaapplekInput = tk.StringVar()
omhakkenInput = tk.IntVar()
bosvliegtuigInput = tk.StringVar()
grotInput = tk.StringVar()
slaapplekInput2 = tk.StringVar()
huisInput = tk.StringVar()
huis2Input = tk.StringVar()
radioInput = tk.StringVar()
frequentieInput = tk.IntVar()
bootInput = tk.StringVar()
getallen = list(range(1,1000))
jaNee = ["Ja","Nee"]
bosVliegtuig = ["Bos", "Vliegtuig"]

verhaaltje1 = """Je hebt net een heftige noodlanding gemaakt omdat een van de motoren van het vliegtuig kapot is gegaan.
Je wordt wakker zonder enig idee waar je bent in het wrak van het neergestortte vliegtuig.
Je loopt naar de opengebarstte achterkant van het vliegtuig en ziet een bijl op de grond liggen.
(Onthoud de frequentie 208)"""
verhaaltje2 = """Vervolgens ga je vanaf het vliegtuig het bos in.
Je hebt nog nergens om de nacht door te brengen dus,"""
verhaaltje3 = """Je gaat het luik naar beneden en komt terecht in een ruimte waarin allemaal spullen staan,
zoals een generator, lampen, een betere bijl en het lijkt erop dat er ook een radio staat.
Je zet de generator aan."""
verhaaltje4 ="""Het lijkt erop dat de radio het nog doet en je besluit contact te zoeken met iemand via de radio.
Je moet een de radio instellen op een frequentie(hij is al eens eerder voorgekomen"""
verhaaltje5 ="""De volgende dag hoor je de boot al in de verte aankomen
Je stapt op de boot zodra die aanmeert en daarmee hebt je get spel gewonnen
-------------------------------------
|             You won!              |
-------------------------------------"""
def incorrect(text):
    messagebox.showinfo("Incorrect",text)
def gameover(text):
    messagebox.showinfo("Gameover",text)
    window.destroy()
def volgende():
    messagebox.showinfo("Correct", "Uitstekende keuze!")

def LevelEenCheck():
    global bijlInput
    antwoord = bijlInput.get()
    if antwoord == "Ja":
        volgende()
        LevelTwee_1()
    elif antwoord == "Nee":
        gameover("Dat was geen goede keuze, je bent in de nacht om het leven gebracht door de monsters op het eiland.")

def LevelTwee_1():
    level.configure(text="Level 2 - Het Bos")
    verhaal.configure(text=verhaaltje2)
    verhaal.place(x=150)
    vraag.configure(text="Ga je een veilige slaapplek maken voor de nacht?")
    vraag.place(x=150)
    antwoordV.configure(textvariable=slaapplekInput)
    button.configure(command=LevelTweeCheck_1)
def LevelTwee_2():
    verhaal.configure(text="Je hebt 10 planken nodig voor een slaapplek, 1 boom = 5 planken.")
    verhaal.place(x=130)
    vraag.configure(text="Hoeveel bomen ga je omhakken voor je slaapplek?")
    antwoordV.configure(textvariable=omhakkenInput,values=getallen)
    button.configure(command=LevelTweeCheck_2)
def LevelTwee_3():
    verhaal.configure(text="Nadat je de hut af had ben je gaan slapen en is het nu dus de volgende ochtend.")
    verhaal.place(x=90)
    vraag.configure(text="Ga je dieper het bos is of ga je naar het vliegtuig om spullen te verzamelen?")
    vraag.place(x=70)
    antwoordV.configure(textvariable=bosvliegtuigInput,values=bosVliegtuig)
    button.configure(command=LevelTweeCheck_3)
def LevelTwee_4():
    verhaal.configure(text="Je gaat dieper het bos in en komt een grot tegen.")
    verhaal.place(x=160)
    vraag.configure(text="Ga je de grot in?")
    vraag.place(x=270)
    antwoordV.configure(textvariable=grotInput,values=jaNee)
    button.configure(command=LevelTweeCheck_4)
def LevelTwee_5():
    verhaal.configure(text="Het wordt nacht.")
    verhaal.place(x=265)
    vraag.configure(text="Ga je terug naar je slaapplek?")
    vraag.place(x=230)
    antwoordV.configure(textvariable=slaapplekInput2,values=jaNee)
    button.configure(command=LevelTweeCheck_5)
def LevelTwee_6():
    verhaal.configure(text="Je gaat verder het bos in en vindt een verlaten huis.")
    verhaal.place(x=160)
    vraag.configure(text="Ga je het huis in?")
    vraag.place(x=250)
    antwoordV.configure(textvariable=huisInput,values=jaNee)
    button.configure(command=LevelTweeCheck_6)
def LevelDrie():
    level.configure(text="Level 3 - Het huis")
    verhaal.configure(text="Binnen in het huis ziet het er erg verlaten uit, maar er valt wat op in de grond.\nHet is een luik in de grond van het huis ")
    verhaal.place(x=110)
    vraag.configure(text="Ga je naar beneden in het luik?")
    vraag.place(x=210)
    antwoordV.configure(textvariable=huis2Input,values=jaNee)
    button.configure(command=LevelDrieCheck)
def LevelVier():
    level.configure(text="Level 4 - de Kelder")
    verhaal.configure(text=verhaaltje3)
    verhaal.place(x=50)
    vraag.configure(text="Ga je de radio gebruiken?")
    vraag.place(x=230)
    antwoordV.configure(textvariable=radioInput,values=jaNee)
    button.configure(command=LevelVierCheck_1)
def LevelVier_2():
    verhaal.configure(text=verhaaltje4)
    verhaal.place(x=50)
    vraag.configure(text="Welke kies je?")
    vraag.place(x=260)
    antwoordV.configure(textvariable=frequentieInput,values=getallen)
    button.configure(command=LevelVierCheck_2)
def LevelVier_3():
    verhaal.configure(text="De man op de radio stelt voor om een boot te varen richting het eiland.")
    verhaal.place(x=120)
    vraag.configure(text="Neem je dit offer aan? ")
    vraag.place(x=240)
    antwoordV.configure(textvariable=bootInput,values=jaNee)
    button.configure(command=LevelVierCheck_3)
def Ending():
    verhaal.configure(text=verhaaltje5)
    verhaal.place(x=70)
    vraag.destroy()
    antwoordV.destroy()
    button.configure(command=window.destroy,text="Afsluiten")

def LevelTweeCheck_1():
    antwoord = slaapplekInput.get()
    if antwoord == "Ja":
        volgende()
        LevelTwee_2()
    else:
        gameover("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")
def LevelTweeCheck_2():
    antwoord = omhakkenInput.get()
    if antwoord >= 2:
        volgende()
        LevelTwee_3()
    else:
        gameover("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")
def LevelTweeCheck_3():
    antwoord = bosvliegtuigInput.get()
    if antwoord== "Bos":
        volgende()
        LevelTwee_4()
    elif antwoord == "Vliegtuig":
        gameover("Je komt aan bij het vliegtuig en er springt ineens een monster op je vanuit de cockpit.")
    else:
        incorrect("Incorrecte keuze, gebruik de woorden 'bos' of 'vliegtuig'.")
def LevelTweeCheck_4():
    antwoord = grotInput.get()
    if antwoord == "Nee":
        volgende()
        LevelTwee_5()
    else:
        gameover("Je bent de grot van een beer in gegaan en wordt vermoord.")
def LevelTweeCheck_5():
    antwoord = slaapplekInput2.get()
    if antwoord == "Nee":
        volgende()
        LevelTwee_6()
    else:
        gameover("Op de weg terug naar je slaapplek wordt je overvallen door een monster op het eiland.")
def LevelTweeCheck_6():
    antwoord = huisInput.get()
    if antwoord == "Ja":
        volgende()
        LevelDrie()
    else:
        gameover("Het is nog nacht en dus komt er een monster uit de bosjes tevoorschijn die jouw vermoord.")
def LevelDrieCheck():
    antwoord = huis2Input.get()
    if antwoord == "Ja":
        volgende()
        LevelVier()
    else:
        gameover("Het is nog nacht en er komt een monster het huis in die je om het leven brengt.")
def LevelVierCheck_1():
    antwoord = radioInput.get()
    if antwoord.lower().strip() == "ja":
        volgende()
        LevelVier_2()
    else:
        gameover("Je hebt gekozen de radio niet te gebruiken, maar het is de enige manier van het eiland af.")
def LevelVierCheck_2():
    antwoord = frequentieInput.get()
    if antwoord == 208:
        volgende()
        LevelVier_3()
    else:
        gameover("Dit is niet de correcte frequentie en daarmee heb je gefaald om iemand te bereiken aan de andere kant van de radio.")
def LevelVierCheck_3():
    antwoord = bootInput.get()
    if antwoord == "Ja":
        volgende()
        Ending()
    else:
        gameover("Je hebt het offer niet aangenomen en daarmee hebt je de verkeerde keuze gemaakt. De boot is de enige manier van het eiland af.")
        
level = tk.Label(text="Level 1 - Vliegtuig",font=("Calibri Light", 11, font.BOLD))
level.place(y=0,x=255)
verhaal = tk.Label(text=verhaaltje1, font=("Calibri Light", 11))
verhaal.place(y=20,x=5)
vraag = tk.Label(text="Neem je de bijl mee?", font=("Calibri Light", 12))
vraag.place(y=120,x=250)
antwoordV = ttk.Combobox(width=10,values=jaNee,textvariable=bijlInput, font=("Calibri Light", 12))
antwoordV.place(y=150,x=270)
button = tk.Button(width=10,text="Volgende",bd=0.5,command=LevelEenCheck)
button.place(y=200,x=280)

window.mainloop()