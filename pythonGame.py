from cgitb import text
from optparse import Values
import tkinter as tk
from tkinter import font, ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Adventure Game GUI Update")
window.geometry("650x250")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)]

bijlInput = tk.StringVar()
slaapplekInput = tk.StringVar()
omhakkenInput = tk.StringVar()
getallen = list(range(1,100))
jaNee = ["Ja","Nee"]
verhaaltje1 = """Je hebt net een heftige noodlanding gemaakt omdat een van de motoren van het vliegtuig kapot is gegaan.
Je wordt wakker zonder enig idee waar je bent in het wrak van het neergestortte vliegtuig.
Je loopt naar de opengebarstte achterkant van het vliegtuig en ziet een bijl op de grond liggen.
(Onthoud de frequentie 208)"""
verhaaltje2 = """Vervolgens ga je vanaf het vliegtuig het bos in.
Je hebt nog nergens om de nacht door te brengen dus,
"""

def gameover(text):
    messagebox.showinfo("Gameover",text)
    window.destroy()

def volgende():
    messagebox.showinfo("", "Uitstekende keuze!")

def LevelEen():
    global bijlInput
    antwoord = bijlInput.get()
    if antwoord == "Ja":
        print("Goede keuze!")
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
    vraag.configure(text="Hoeveel bomen ga je omhakken voor je slaapplek?")
    antwoordV.configure(textvariable=omhakkenInput,values=getallen)
    button.configure(command=LevelTweeCheck_2)

def LevelTwee_3():
    verhaal.configure(text="Je hebt 10 planken nodig voor een slaapplek, 1 boom = 5 planken.")
    vraag.configure(text="Hoeveel bomen ga je omhakken voor je slaapplek?")
    antwoordV.configure(textvariable=omhakkenInput,values=getallen)
    button.configure(command=LevelTweeCheck_2)

def LevelTweeCheck_1():
    antwoord = slaapplekInput.get()
    if antwoord == "Ja":
        volgende()
        LevelTwee_2()
    else:
        gameover("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")
def LevelTweeCheck_2():
    antwoord1 = omhakkenInput.get()
    if antwoord1 >= 2:
        print("Goede keuze!")
        print()
        print("Nadat je de hut af had ben je gaan slapen en is het nu dus de volgende ochtend.")
        print("Je moet een keuze maken, ga je dieper het bos is of ga je naar het vliegtuig om spullen te verzamelen?")
        print("- Bos")
        print("- Vliegtuig")
        #bos_level2()
    else:
        gameover("Je faalt om jezelf in de nacht te beschermen tegen de monsters op het eiland.")








level = tk.Label(text="Level 1 - Vliegtuig",font=("Calibri Light", 11, font.BOLD))
level.place(y=0,x=255)
verhaal = tk.Label(text=verhaaltje1, font=("Calibri Light", 11))
verhaal.place(y=20,x=5)
vraag = tk.Label(text="Neem je de bijl mee?", font=("Calibri Light", 12))
vraag.place(y=120,x=250)
antwoordV = ttk.Combobox(width=10,values=jaNee,textvariable=bijlInput, font=("Calibri Light", 12))
antwoordV.place(y=150,x=270)
button = tk.Button(width=10,text="Volgende",bd=0.5,command=LevelEen)
button.place(y=200,x=280)

window.mainloop()