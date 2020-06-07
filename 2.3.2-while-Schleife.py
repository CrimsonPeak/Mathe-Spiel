# Der Benutzer soll eine Matheaufgabe lösen, die random gestellt wird
# Der Benutzer wählt seine Rechnungsart aus durch einem Menü
import random

option = ""
while(option != "0"):
    countVersuche = 1
    countRechnung = 1
    wertebereich = 5

    print("\nHauptmenü")
    print("\nGeben Sie die gewünschte Zahl ein")
    print("""0 : Exit
1 : Addition
2 : Multiplikation
3 : Division
4 : Subtraktion\n""")

    print("Ihre Eingabe", end=": ")
    option = input()

    #Für 0 = Exit
    if(option == "0"):
        print("Sie haben das Programm beendet")
        break

    while(countVersuche <= 3):
        #Random Zahl zwischen 0 und max
        x = random.randint(0, wertebereich)
        y = random.randint(0, wertebereich)

        #Für 1 = Addition
        if(option == "1"):
            operator = "+"
            erg = x + y

        #Für 2 = Multiplikation
        elif(option == "2"):
            operator = "*"
            erg = x * y

        #Für 3 = Division
        elif(option == "3"):
            operator = "/"
            erg = x / y

        #Für 4 = Subtraktion
        elif(option == "4"):
            operator = "-"
            erg = x - y

        # Die Aufgabe wird angezeigt und das Ergebnis eingegeben
        print(x, operator, y, end=" = ")
        ergEingabe = int(input())

        if(erg == ergEingabe):
            print("Richtig!")

            # Alle 5 Runden wird der Wertebereich um 5 erhöht
            if(countRechnung == 5):
                countRechnung = 1
                wertebereich = wertebereich + 5
            else:
                countRechnung = countRechnung + 1

        else:
            countVersuche = countVersuche + 1
            print("Falsch")