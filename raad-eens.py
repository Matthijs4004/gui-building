from cgitb import text
from distutils import command
import glob
import random
import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("Raad eens (GUI Update)")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

round = 0
score = 0
count = 0
num = random.randint(0, 1000)
getal = tk.IntVar()

def destroyGame():
    vorigeGok.destroy()
    getalInput.destroy()
    kleinerGroter.destroy()
    gegokt.destroy()

def destroyMain():
    uitleg1.destroy()
    uitleg2.destroy()
    uitleg3.destroy()
    button.configure(text="Start",command=StartGame)
    button.place(y=240,x=130)
    
def StartGame():
    global kleinerGroter, vorigeGok, gegokt, getalInput
    vorigeGok = tk.Label(text="Vorige gok: 000",font=("Calibri Light", 11))
    vorigeGok.place(y=80,x=100)
    gegokt = tk.Label(text="Doe een gok",font=("Calibri Light", 14))
    gegokt.place(y=110,x=100)
    getalInput = tk.Entry(textvariable=getal, width=8,font=("Calibri Light", 12))
    getalInput.place(y=140,x=115)
    kleinerGroter = tk.Label(text="",font=("Calibri Light", 11))
    kleinerGroter.place(y=190,x=80)
    button.configure(text="Gok",command=gokken)

def gokken():
    global count
    count += 1
    gok = getal.get()
    vorigeGok.configure(text="Vorige gok: "+str(gok))
    if num == gok:
        print("Goed gedaan! Je hebt ",count, " gokken gedaan voordat je het goed had. Score: ", score)
    elif num > gok:
        kleinerGroter.configure(text="Je hebt te klein gegokt!")
    elif num < gok:
        kleinerGroter.configure(text="Je hebt te hoog gegokt!")

    if count >= 10:
        eindScherm()

def eindScherm():
    destroyGame()
    eindstand = tk.Label(text="Het getal was "+str(num),font=("Calibri Light", 14))
    eindstand.place(y=110,x=80)
    button.configure(text="Opnieuw proberen", command=StartGame)
    button.place(y=240,x=85)
    
titel = tk.Label(text="Raad het getal",font=("Calibri Light", 20))
titel.place(y=5,x=70)

uitleg1 = tk.Label(text="De computer kiest een getal tussen de 0 en 1000",font=("Calibri Light", 10))
uitleg1.place(y=50,x=20)
uitleg2 = tk.Label(text="Jij moet proberen het getal te raden",font=("Calibri Light", 10))
uitleg2.place(y=70,x=50)
uitleg3 = tk.Label(text="Je hebt 10 kansen voordat de computer heeft gewonnen",font=("Calibri Light", 10))
uitleg3.place(y=90,x=0.1)

button = tk.Button(text="Volgende",bd=0.5,font=("Calibri Light", 12),command=destroyMain)
button.place(y=240,x=115)


window.mainloop()