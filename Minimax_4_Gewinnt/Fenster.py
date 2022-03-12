import tkinter
import Spielfeld
import ZeichenProzesse
import Minimax
zeichner = ZeichenProzesse.Zeichne()

#------------------------UI wird Initzialisiert----------------------------------------------------------------------------------------------------------------------------
feld = Spielfeld.Feld()
fenster = tkinter.Tk()
sizeX = 350
sizeY = 300
offsetY = 50
displayOffset = 10
fenster.geometry(str(sizeX+2*displayOffset)+"x"+ str(sizeY+offsetY+displayOffset))
cv = tkinter.Canvas(fenster,width = sizeX+2*displayOffset, height=(sizeY+offsetY))
cv.pack()
zeichner.ZeichneTrennLinien([cv,sizeX,sizeY,displayOffset,offsetY])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
minimax = Minimax.MinimaxAlgorithm()
test = 0

clicks = 1

#SpielerModus 0 = SPieler gegen Spieler, Spielermodus 1 = Spieler gegen KI, SPielermodus 2 = KI gegen KI
spielerModus = 1

angeklicktesFeld = 0

kannNächstenZugMachen = 0

spielerAmZug = 1
spielAktiv = True

#--------------------Spieler drückt Maus Event----------------------------------------------------------------------------------------------------------------------------
def click(event):
    global test
    global kannNächstenZugMachen
    global angeklicktesFeld
    global spielerAmZug
    global spielAktiv
    if spielAktiv:
        posX = event.x
        feldX = feld.PixelKoordinatenZuFeldPosition(posX,sizeX,displayOffset)
        angeklicktesFeld = feldX
        platziereFigur(feldX)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def platziereFigur(feldX):
    global feld
    global spielerAmZug
    global spielAktiv
    global minimax
    if spielAktiv == True:
        if feldX != 999:
                if feld.SpalteIstVoll(feldX) != True:
                    #Physik gibt die neue Y Position zurück
                    feldY = feld.Physik(feldX)
                    feld.feldPositionen[feldX][feldY] = spielerAmZug
                    #Die Figur wird gezeichnet.
                    zeichner.ZeichneFigur(feldX,feldY,spielerAmZug)
                    #Es wird geprüft ob ein Spieler gewonnen hat.
                    anzahlDerFigurenInReihe = feld.FigurenInReihePrüfung(spielerAmZug)
                    if anzahlDerFigurenInReihe < 4:
                        wechsleSpielerAmZug()
                        
                    else:
                        print("Spieler " + str(spielerAmZug) + "hat gewonnen!")
                        spielAktiv = False
                else:
                    print("FEHLER")


    
def wechsleSpielerAmZug():
    global spielerAmZug
    global spielerModus
    global feld
    global minimax
    if spielerAmZug == 1:
        spielerAmZug = -1
    elif spielerAmZug == -1:
        spielerAmZug = 1
    if spielerModus != 0 and spielerAmZug == -1:
        zug = minimax.BesterZug(feld,4,-1)
        platziereFigur(zug[0])





fenster.bind('<Button-1>',click)
fenster.mainloop()
