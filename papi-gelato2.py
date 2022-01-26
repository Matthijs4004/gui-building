# Nieuwe versie van papi gelato (Matthijs Raatgever)


# Het gaat goed met Papi Gelato en ze gaan het assortiment uitbreiden. Hiervoor moeten wel wat aanpassingen gedaan worden aan het programmaatje dat je hebt geschreven.
# Ze gaan toppings verkopen, na dat de verkoper weet of hij/zij een hoorntje of bakje moet gebruiken wordt de vraag gesteld: “Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?”.

# Iedere topping heeft zo zijn eigen prijs, maar alle toppings staan als 1 regel op het bonnetje.
# Geen: geen extra kosten
# Slagroom: €0,50 extra kosten
# Sprinkels: voor ieder bolletje €0,30 extra kosten
# Caramel Saus: als de bestelling in een horrentje zit dan €0,60 extra kosten, als het in een bakje zit dan €0,90 extra kosten.

# Het komt er dan zo uit te zien bij het bestellen van een bakje met 4 bolletjes en slagroom + een horrentje met 1 bolletje en saus:
# Bij een andere keuze dan A, B, C of D krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald
# Als er geen toppings zijn gekozen komt de regel met toppings niet op het bonnetje.



alleToppings = 0
topping = 0
aantalBolletjes = 0
aantalHoorntjes = 0
aantalBakjes = 0
aantalSlagroom = 0
aantalSprinkels = 0
aantalCaramel = 0
slagroomPrijs = 0.50
sprinkelsPrijs = 0.30
caramelHoorntje = 0.60
caramelBakje = 0.90
bolletjePrijs = 0.95
hoorntjePrijs = 1.25
bakjePrijs = 0.7


# Code
print("Welkom bij Papi Gelato.\n")

def showError():
    print('Sorry, dat snap ik niet...')

def showErrorB():
    print('Sorry, zulke grote bakken hebben we niet')

def bon():
    global alleToppings
    totaalBol = aantalBolletjes * bolletjePrijs
    totaalHoorntje = aantalHoorntjes * hoorntjePrijs
    totaalBak = aantalBakjes * bakjePrijs
    totaalTopping = aantalSlagroom + aantalCaramel + aantalSprinkels
    totaalBedrag = totaalBol + totaalHoorntje + totaalBak + totaalTopping
    alleToppings += topping
    print('--------------[Papi Gelato]--------------')
    print()
    if aantalBolletjes >= 1:
        print('Bolletjes        '+ str(aantalBolletjes) +' x €0.95 = €'+ str(round(totaalBol, 3)))
    if aantalHoorntjes >= 1:
        print('Hoorntje         '+ str(aantalHoorntjes) +' x €1,25 = €' + str(round(totaalHoorntje, 3)))
    if aantalBakjes >= 1:
        print('Bakje            '+ str(aantalBakjes) +' x €0,75 = €'+ str(round(totaalBak, 3)))
    if topping >= 1:
        print('Topping          '+ str(alleToppings) +' x €'+ str(round(totaalTopping, 3)) +' = €'+ str(round(totaalTopping, 3)))
    print('                             ----- +')
    print('Totaal:                      €'+ str(round(totaalBedrag, 3)))

def start(): #stap 1
    global aantalBolletjes, bolInput, aantalBakjes, alBakje, houder
    alBakje = False
    bolInput = int(input("Hoeveel bolletjes wilt u? "))
    aantalBolletjes += bolInput
    if bolInput in range(1,4):
        smaakKeuze()
    elif bolInput in range(4,8):
        print("Dan krijgt u van mij een bakje met ",bolInput," bolletjes")
        aantalBakjes += 1
        alBakje = True
        houder = "bakje"
        smaakKeuze()
    elif bolInput > 8:
        showErrorB()
        start()
    else:
        showError()
        start()

def smaakKeuze(): # smaken
    for x in range(bolInput, 0, -1):
        smaak = input("Welke smaak wilt u voor bolletje nummer " + str(x) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille ")
    if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
        if alBakje == True:
            toppings()
        else:
            BakjeOfHoorntje()
    else:
        showError()
        smaakKeuze()

def toppings(): # toppings
    global topping, aantalSlagroom, aantalSprinkels, aantalCaramel
    print()
    ToppingVraag = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ').upper()
    if ToppingVraag == "A" or ToppingVraag == "Geen":
        topping = 0
        opnieuw()
    elif ToppingVraag == "B" or ToppingVraag == "Slagroom":
        aantalSlagroom += slagroomPrijs
        topping =+ 1
        opnieuw()
    elif ToppingVraag == "C" or ToppingVraag == "Sprinkels":
        aantalSprinkels += sprinkelsPrijs * aantalBolletjes
        topping =+ 1
        opnieuw()
    elif ToppingVraag == "D" or ToppingVraag == "Caramel saus" or ToppingVraag == "Caramel":
        if houder == "A" or houder == "hoorntje":
            aantalCaramel += caramelHoorntje
        if houder == "B" or houder == "bakje":
            aantalCaramel += caramelBakje
        topping =+ 1
        opnieuw()
    else:
        showError()
    topping += topping
    if bolInput >= 4:
        opnieuw()

def BakjeOfHoorntje(): #stap 2
    global houder, aantalHoorntjes, aantalBakjes
    houder = input("Wilt u deze "+ str(bolInput) +" bolletje(s) in A) een hoorntje of B) een bakje? ")
    if houder == "A" or houder == "hoorntje":
        houder = "hoorntje"
        aantalHoorntjes += 1
        toppings()
        opnieuw()
    elif houder == "B" or houder == "bakje":
        houder = "bakje"
        aantalBakjes += 1
        toppings()
        opnieuw()
    else:
        showError()
        BakjeOfHoorntje()

def opnieuw(): #stap 3
    nogmaals = input("\nHier is uw "+str(houder)+" met "+str(bolInput)+" bolletje(s). Wilt u nog meer bestellen? Y/N ")
    if nogmaals == "Y":
        start()
    elif nogmaals == "N":
        bon()
        print("Bedankt en tot ziens!")
    else:
        showError()
        opnieuw()


start()
