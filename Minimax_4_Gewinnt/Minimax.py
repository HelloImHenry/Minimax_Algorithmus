import Spielfeld

class MinimaxAlgorithm:
    feld = []
    eingegebeneTiefe = 0
    #WIKI
    gespeicherterZug = [99,99]
    def miniMax(self,spieler,tiefe):
        if tiefe == 0 or self.feld.SpielFeldVoll() == True:
            return self.evaluiere(spieler)
        maxWert = -1000000000000
        züge = self.generiereMöglicheZüge()
        for x in range(len(züge)):
            posX = züge[x][0]
            posY = züge[x][1]
            self.feld.feldPositionen[posX][posY] = spieler
            wert = self.miniMax((-spieler),(tiefe-1))
            wert = wert*-1
            self.feld.feldPositionen[posX][posY] = 0
            if wert > maxWert:
                maxWert = wert
                if tiefe == self.eingegebeneTiefe:
                    self.gespeicherterZug = [posX,posY]
        return maxWert
    def generiereMöglicheZüge(self):
        möglicheZüge = []
        for x in range(7):
            if self.feld.SpalteIstVoll(x) == False:
                y = self.feld.Physik(x)
                möglicheZüge.append([x,y])
        return möglicheZüge
    belohnungen = [0,5,10,500,100000]
    def evaluiere(self,spieler):
        evaluierterWert = 0
        for n in range(len(self.feld.gewinnKombinationen)):
            spielerFiguren = 0
            gegnerFiguren = 0
            zuUntersuchendeKombination = self.feld.gewinnKombinationen[n]
            for x in range(4):
                zuUntersuchendesFeld = zuUntersuchendeKombination[x]
                feldX = zuUntersuchendesFeld[0]
                feldY = zuUntersuchendesFeld[1]
                if self.feld.feldPositionen[feldX][feldY] == spieler:
                    spielerFiguren = spielerFiguren+1
                elif self.feld.feldPositionen[feldX][feldY] == -spieler:
                    gegnerFiguren = gegnerFiguren+1
            if spielerFiguren == 4:
                evaluierterWert = evaluierterWert + 100000
            elif spielerFiguren == 3 and gegnerFiguren == 0:
                evaluierterWert = evaluierterWert + 500
            elif spielerFiguren == 2 and gegnerFiguren == 0:
                evaluierterWert = evaluierterWert + 10
            elif spielerFiguren == 1 and gegnerFiguren == 0:
                evaluierterWert = evaluierterWert + 5
            elif gegnerFiguren == 4:
                evaluierterWert = evaluierterWert - 100000
            elif spielerFiguren == 0 and gegnerFiguren == 3:
                evaluierterWert = evaluierterWert - 500
            elif spielerFiguren == 0 and gegnerFiguren == 2:
                evaluierterWert = evaluierterWert - 10
            elif spielerFiguren == 0 and gegnerFiguren == 1:
                evaluierterWert = evaluierterWert - 5
                
            evaluierterWert = evaluierterWert
        return evaluierterWert
    def BesterZug(self,feld,tiefe,spieler):
        self.eingegebeneTiefe = tiefe
        self.feld = feld
        bewerten = self.miniMax(spieler,tiefe)
        if self.gespeicherterZug != [99,99]:
            return self.gespeicherterZug
