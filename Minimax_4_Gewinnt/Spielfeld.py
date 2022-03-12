class Feld:
    gewinnKombinationen = []
    def __init__(self):
        #x y
        self.feldPositionen = []
        for x in range(7):
            self.feldPositionen.append([0,0,0,0,0,0])
        self.generiereGewinnKombinationen()
    def generiereGewinnKombinationen(self):
        #Breite
        for y in range(6):
            for x in range(4):
                gewinnKombination = []
                for n in range(4):
                    gewinnKombination.append([(x+n),y])
                self.gewinnKombinationen.append(gewinnKombination)
        #Höhe
        for x in range(7):
            for y in range(3):
                gewinnKombination = []
                for n in range(4):
                    gewinnKombination.append([x,(y+n)])
                self.gewinnKombinationen.append(gewinnKombination)
        #RechtsObenZuLinksUnten
        for x in range(4):
            for y in range(3):
                gewinnKombination = []
                for n in range(4):
                    gewinnKombination.append([(x+n),(y+n)])
                self.gewinnKombinationen.append(gewinnKombination)
        #RechtsUntenZuLinksOben
        for x in range(3,7):
            for y in range(3):
                gewinnKombination = []
                for n in range(4):
                    gewinnKombination.append([(x-n),(y+n)])
                self.gewinnKombinationen.append(gewinnKombination)
    #Verschiebt die Figur nach unten (Platziert sie aber nicht.)
    def Physik(self,posX):
        #Die derzeitige Höhe
        derzeitigesY = 5
        while self.feldPositionen[posX][derzeitigesY] == 0 and derzeitigesY > -1:
            derzeitigesY = derzeitigesY-1
        derzeitigesY+=1
        return derzeitigesY
    #Ermittelt Falls mögliche den Gewinner oder ein Unentschieden
    def FigurenInReihePrüfung(self,spieler):
        derzeitigeKombinationen = 0
        for n in range(len(self.gewinnKombinationen)):
            inKombination = 0
            kombination = self.gewinnKombinationen[n]
            for x in range(4):
                feld = kombination[x]
                if self.feldPositionen[feld[0]][feld[1]] == spieler:
                    inKombination = inKombination+1
                else:
                    break
            if inKombination>derzeitigeKombinationen:
                derzeitigeKombinationen = inKombination
        
                
        return derzeitigeKombinationen
    #Nimmt als Parameter die MausPosition posX und die Spielfeldgröße X
    def PixelKoordinatenZuFeldPosition(self,posX,sizeX,offsetX):
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
    def SpalteIstVoll(self,x):
        if self.feldPositionen[x][5] != 0:
            return True
        else:
            return False
    #Prüft ob das SPielfeld voll ist. Falls ja return die Funktion true, fals nein false
    def SpielFeldVoll(self):
        output = True
        for x in range(7):
            if self.feldPositionen[x][5] == 0:
                output = False
                break
        return output