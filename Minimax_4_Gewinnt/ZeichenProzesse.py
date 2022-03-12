class Zeichne:
    zeichenObjekte = []
    uiParameter = []
    spielerFarben = ["#0000FF","#FFFF00","#00BFFF","#DBA901"]
        #cv,sizeX,sizeY,displayOffset,offsetY
    def ZeichneTrennLinien(self,uiInput):
        self.uiParameter.clear()
        for x in range(5):
            self.uiParameter.append(uiInput[x])
        curPos = 0
        for x in range(8):
            id = uiInput[0].create_line((uiInput[3]+curPos),(uiInput[4]),(uiInput[3]+curPos),uiInput[2]+uiInput[4])
            self.zeichenObjekte.append(id)
            curPos = curPos + (uiInput[1]/7)
        curPos = 0
        for x in range(7):
            id = uiInput[0].create_line(uiInput[3],(curPos+uiInput[4]),uiInput[1]+uiInput[3],(curPos+uiInput[4]))
            curPos = curPos + (uiInput[2]/6)
            self.zeichenObjekte.append(id)
            
    def ZeichneFigur(self,x,y,spieler):
        untenLinksY = self.uiParameter[2] + self.uiParameter[4]-(y*(self.uiParameter[2]/6))
        id = self.uiParameter[0].create_oval(((x*(self.uiParameter[1]/7))+self.uiParameter[3]), (untenLinksY),((x*(self.uiParameter[1]/7))+ (self.uiParameter[1]/7) + self.uiParameter[3]),(untenLinksY - (self.uiParameter[2]/6)), fill = self.spielerFarben[self.UmwandlungSpielerAmZugZuFarbID(spieler)])
        self.zeichenObjekte.append(id)

    def UmwandlungSpielerAmZugZuFarbID(self,spieler):
        if spieler == -1:
            return 0
        if spieler == 1:
            return 1
