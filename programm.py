from json.encoder import INFINITY
import tkinter
import ZeichenProzesse
spielFeld = []
gewinnKombinationen = []
def generiereGewinnKombinationen():
    #Breite
    for y in range(6):
        for x in range(4):
            gewinnKombination = []
            for n in range(4):
                gewinnKombination.append([(x+n),y])
            gewinnKombinationen.append(gewinnKombination)
    #Höhe
    for x in range(7):
        for y in range(3):
            gewinnKombination = []
            for n in range(4):
                gewinnKombination.append([x,(y+n)])
            gewinnKombinationen.append(gewinnKombination)
    #RechtsObenZuLinksUnten
    for x in range(4):
        for y in range(3):
            gewinnKombination = []
            for n in range(4):
                gewinnKombination.append([(x+n),(y+n)])
            gewinnKombinationen.append(gewinnKombination)
    #RechtsUntenZuLinksOben
    for x in range(3,7):
        for y in range(3):
            gewinnKombination = []
            for n in range(4):
                gewinnKombination.append([(x-n),(y+n)])
            gewinnKombinationen.append(gewinnKombination)
generiereGewinnKombinationen()
def erstelleSpielFeld():
    for x in range(7):
        spielFeld.append([0,0,0,0,0,0])
erstelleSpielFeld()
#------------------------UI wird Initzialisiert----------------------------------------------------------------------------------------------------------------------------
fenster = tkinter.Tk()
sizeX = 350
sizeY = 300
offsetY = 50
displayOffset = 10
fenster.geometry(str(sizeX+2*displayOffset)+"x"+ str(sizeY+offsetY+displayOffset))
cv = tkinter.Canvas(fenster,width = sizeX+2*displayOffset, height=(sizeY+offsetY))
cv.pack()
def ZeichneTrennLinien(uiInput):
    uiParameter.clear()
    for x in range(5):
        uiParameter.append(uiInput[x])
    curPos = 0
    for x in range(8):
        id = uiInput[0].create_line((uiInput[3]+curPos),(uiInput[4]),(uiInput[3]+curPos),uiInput[2]+uiInput[4])
        zeichenObjekte.append(id)
        curPos = curPos + (uiInput[1]/7)
    curPos = 0
    for x in range(7):
        id = uiInput[0].create_line(uiInput[3],(curPos+uiInput[4]),uiInput[1]+uiInput[3],(curPos+uiInput[4]))
        curPos = curPos + (uiInput[2]/6)
        zeichenObjekte.append(id)
ZeichneTrennLinien([cv,sizeX,sizeY,displayOffset,offsetY])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        feldX = MausPositionZuFeld(posX,sizeX,displayOffset)
        angeklicktesFeld = feldX
        platziereFigur(feldX)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def platziereFigur(feldX):
    global spielerAmZug
    global spielAktiv
    if spielAktiv == True:
        if feldX != 999:
            if SpalteIstVoll(feldX) != True:
                #Physik gibt die neue Y Position zurück
                feldY = Physik(feldX)
                spielFeld[feldX][feldY] = spielerAmZug
                #Die Figur wird gezeichnet.
                ZeichneFigur(feldX,feldY,spielerAmZug)
                #Es wird geprüft ob ein Spieler gewonnen hat.
                anzahlDerFigurenInReihe = FigurenInReihePrüfung(spielerAmZug)
                print(str(anzahlDerFigurenInReihe))
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
    if spielerAmZug == 1:
        spielerAmZug = -1
    elif spielerAmZug == -1:
        spielerAmZug = 1
    if spielerModus != 0 and spielerAmZug == -1:
        zug = BesterZug(7,-1)
        platziereFigur(zug[0])





def Physik(x):
    global gespeicherterZug
    global spielFeld
    derzeitigesY = 5
    while spielFeld[x][derzeitigesY] == 0 and derzeitigesY != -1:
        derzeitigesY -=1
    derzeitigesY+=1
    return derzeitigesY
def MausPositionZuFeld(posX,sizeX,offsetX):
    #Enthält die Koordinaten ab denen ein neues Feld beginnt. Es wird nur nach x unterschieden, da y irrelevant istz
    pixelPos = []
    #Speichert die derzeitige Position des For Loops. Es wird nicht bei 0 sondern beim Offset gestartet.
    curPixelPos = offsetX
    #Enthält den Rückgabewert, sprich das angeclickte Feld. Wenn der Wert 999 bleibt hat ein Spieler außerhalb des Bildschirm geclickt.
    pos = 999
    for z in range(8):
        pixelPos.append(curPixelPos)
        #/7 Weil es sieben Felder in x gibt.
        curPixelPos=curPixelPos + (sizeX/7)
    for x in range(7):
        if posX >= pixelPos[x] and posX < pixelPos[(x+1)]:
            pos = x
            break
    return pos



def FigurenInReihePrüfung(spieler):
    derzeitigeKombinationen = 0
    for n in range(len(gewinnKombinationen)):
        inKombination = 0
        kombination = gewinnKombinationen[n]
        for x in range(4):
            feld = kombination[x]
            if spielFeld[feld[0]][feld[1]] == spieler:
                inKombination = inKombination+1
        if inKombination>derzeitigeKombinationen:
            derzeitigeKombinationen = inKombination
        
                
    return derzeitigeKombinationen

def SpalteIstVoll(x):
    if spielFeld[x][5] != 0:
        return True
    else:
        return False
def SpielFeldVoll():
    for x in range(7):
        if spielFeld[x][5] == 0:
            return False
    return True
eingegebeneTiefe = 4
gespeicherterZug = [0,0]
def maximieren(spieler,tiefe,alpha,beta):
    global gespeicherterZug
    global spielFeld
    if tiefe == 0 or SpielFeldVoll() == True or FigurenInReihePrüfung(-1) == 4 or FigurenInReihePrüfung(1) == 4:
        if tiefe == 0:
            return evaluiere(spieler)
        if SpielFeldVoll():
            return 0
        if FigurenInReihePrüfung(-1) == 4:
            return 10000000
        if FigurenInReihePrüfung(1) == 4:
            return -1000000
    maxWert = alpha
    züge = generiereMöglicheZüge()
    for x in züge:
        spielFeld[x[0]][x[1]] = spieler
        wert = minimieren(-spieler,tiefe-1,maxWert,beta)
        spielFeld[x[0]][x[1]] = 0
        if wert > maxWert:
            maxWert = wert
            if tiefe == eingegebeneTiefe:
                gespeicherterZug = x
            if maxWert >= beta:
                break
    return maxWert

def minimieren(spieler,tiefe,alpha,beta):
    global gespeicherterZug
    global spielFeld
    if tiefe == 0 or SpielFeldVoll() == True or FigurenInReihePrüfung(-1) == 4 or FigurenInReihePrüfung(1) == 4:
        if tiefe == 0:
            return evaluiere(spieler)
        if SpielFeldVoll():
            return 0
        if FigurenInReihePrüfung(-1) == 4:
            return 10000000
        if FigurenInReihePrüfung(1) == 4:
            return -1000000
    minWert = beta
    züge = generiereMöglicheZüge()
    for x in züge:
        spielFeld[x[0]][x[1]] = spieler
        wert = maximieren(-spieler,tiefe-1,alpha,minWert)
        spielFeld[x[0]][x[1]] = 0
        if wert < minWert:
            minWert = wert
            if minWert <= alpha:
                break
    return minWert
    
def generiereMöglicheZüge():
    global gespeicherterZug
    global spielFeld
    möglicheZüge = []
    for x in range(7):
        if SpalteIstVoll(x) == False:
            y = Physik(x)
            möglicheZüge.append([x,y])
    return möglicheZüge


def evaluiere(spieler):
    global gespeicherterZug
    global spielFeld
    evaluierterWert = 0
    for n in range(len(gewinnKombinationen)):
        spielerFiguren = 0
        gegnerFiguren = 0
        zuUntersuchendeKombination = gewinnKombinationen[n]
        for x in range(4):
            zuUntersuchendesFeld = zuUntersuchendeKombination[x]
            feldX = zuUntersuchendesFeld[0]
            feldY = zuUntersuchendesFeld[1]
            if spielFeld[feldX][feldY] == spieler:
                spielerFiguren = spielerFiguren+1
            elif spielFeld[feldX][feldY] == -spieler:
                gegnerFiguren = gegnerFiguren+1
            #if str(self.feld.gewinnKombinationen[n]) == "[[3, 0], [4, 0], [5, 0], [6, 0]]":
                #print(str(gegnerFiguren) + "_____")
        if spielerFiguren == 4:
            evaluierterWert = evaluierterWert + 100
        if spielerFiguren == 3 and gegnerFiguren == 0:
            evaluierterWert = evaluierterWert + 50
        elif spielerFiguren == 2 and gegnerFiguren == 0:
            evaluierterWert = evaluierterWert + 10
        if spielerFiguren == 0 and gegnerFiguren == 4:
            evaluierterWert = evaluierterWert - 120
        if spielerFiguren == 0 and gegnerFiguren == 3:
            evaluierterWert = evaluierterWert - 80
        elif spielerFiguren == 0 and gegnerFiguren == 2:
            evaluierterWert = evaluierterWert - 10
    return evaluierterWert

def BesterZug(tiefe,spieler):
    global eingegebeneTiefe
    eingegebeneTiefe = tiefe
    bewerten = maximieren(spieler,tiefe,-INFINITY,INFINITY)
    if gespeicherterZug != [0,0]:
        return gespeicherterZug
    else:
        return gespeicherterZug


zeichenObjekte = []
uiParameter = []
spielerFarben = ["#0000FF","#FFFF00","#00BFFF","#DBA901"]
        #cv,sizeX,sizeY,displayOffset,offsetY

            
def ZeichneFigur(x,y,spieler):
    untenLinksY = uiParameter[2] + uiParameter[4]-(y*(uiParameter[2]/6))
    id = uiParameter[0].create_oval(((x*(uiParameter[1]/7))+uiParameter[3]), (untenLinksY),((x*(uiParameter[1]/7))+ (uiParameter[1]/7) + uiParameter[3]),(untenLinksY - (uiParameter[2]/6)), fill = spielerFarben[UmwandlungSpielerAmZugZuFarbID(spieler)])
    zeichenObjekte.append(id)

def UmwandlungSpielerAmZugZuFarbID(spieler):
    if spieler == -1:
        return 0
    if spieler == 1:
        return 1


fenster.bind('<Button-1>',click)
fenster.mainloop()