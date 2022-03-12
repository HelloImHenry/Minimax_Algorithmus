import tkinter
import random
import math
from Node import treeNode
offsetYToBorder = 20
#Größe des Fensters [VERÄNDERBAR]
sizeY = 900
sizeX = 900
#Verzweigungsfaktor [VERÄNDERBAR]
branching_factor = 3
#Suchtiefe [VERÄNDERBAR]
depth = 3




#Anzahl der Spieleenden
outcomeAmount = branching_factor**depth
if outcomeAmount>= 20 and outcomeAmount < 30:
    sizeX+= (outcomeAmount-20)*100
#Derzeitige Tiefe
current_depth = 0
#Kreisbreite = Kreishöhe
width_Circle = (sizeX-(2*offsetYToBorder))/(outcomeAmount*2-1)
#Abstand zwischen den Kreisen Y
circleCircleOffsetY = (sizeY-(2*offsetYToBorder)-(width_Circle*(depth+1)))/(depth)
#Das Array das die Random generierten Outcomes speichert
outcomes = []
#Speichert die Werte der einzelnen Layer ab
layers = []
#NodeController
tree = []
root = tkinter.Tk()
root.title("Spielbaum")
root.geometry(str(sizeX) + "x" + str(sizeY))
cv = tkinter.Canvas(root, width = sizeX, height = sizeY)
cv.pack()
#Berrechnet den Abstand zwischen den Kreisen (Horizontal)
def calculateCircleCircleOffsetXInLayer(amountOfCircles):
    global branching_factor
    global sizeX
    global width_Circle
    global offsetYToBorder
    circleCircleOffsetX = (sizeX- (amountOfCircles*width_Circle))/amountOfCircles
    return circleCircleOffsetX
#Generiert die Zufallszahlen der tiefsten Ebene
def generateNewOutcomes():
    global outcomeAmount
    global outcomes
    for x in range(outcomeAmount):
        number = random.randint(00,9)
        outcomes.append(number)
    layers.append(outcomes)
#Ermittelt die kleinste Zahl aus einem übergebenen Array an zahlen und gibt den Wert, sowie die Position selbst, zurück.
def minimum(numbers):
    output = [100,0]
    for x in range(len(numbers)):
        if numbers[x] < output[0]:
            output = [numbers[x],x]
    return output
#Ermittelt die größte Zahl aus einem übergebenen Array an zahlen und gibt den Wert, sowie die Position selbst, zurück.
def maximum(numbers):
    output = [-1,0]
    for x in range(len(numbers)):
        if numbers[x] > output[0]:
            output = [numbers[x],x]
    return output
#Ermittelt für eine ganze Ebene die kleinsten Werte, und speichert diese, in layers ab.
def minimiseLayer():
    global outcomes
    global current_depth
    global layers
    global tree
    #Speichert die evaluierten Werte dieser Ebene ab.
    evaluatetLayer = []
    for x in range(int(len(outcomes)/branching_factor)):
        layerValues = layers[current_depth]
        values = layerValues[x*branching_factor:x*branching_factor+(branching_factor)]
        minValue = minimum(values)
        node = treeNode([len(evaluatetLayer),(current_depth+1)],[(branching_factor*x+minValue[1]),current_depth])
        tree.append(node)
        evaluatetLayer.append(minValue[0])
    outcomes = evaluatetLayer
    layers.append(evaluatetLayer)
    current_depth+=1
#Ermittelt für eine ganze Ebene die größten Werte, und speichert diese, in layers ab.
def maximiseLayer():
    global outcomes
    global current_depth
    global layers
    global tree
    #Speichert die evaluierten Werte dieser Ebene ab.
    evaluatetLayer = []
    for x in range(int(len(outcomes)/branching_factor)):
        layerValues = layers[current_depth]
        values = layerValues[x*branching_factor:x*branching_factor+(branching_factor)]
        maxValue = maximum(values)
        node = treeNode([len(evaluatetLayer),(current_depth+1)],[(branching_factor*x+maxValue[1]),current_depth])
        tree.append(node)
        evaluatetLayer.append(maxValue[0])
    outcomes = evaluatetLayer
    layers.append(evaluatetLayer)
    current_depth+=1
#Führ das Maximieren und Minimieren so lange aus, bis der, für den maximierenden Spieler, beste Zug ermittelt ist
def minimax():
    global current_depth
    global depth
    while current_depth < depth :
        if depth%2 == 0:
            if current_depth%2 == 1:
                maximiseLayer()
            elif current_depth%2 == 0:
                minimiseLayer()
        else:
            if current_depth%2 == 0:
                maximiseLayer()
            elif current_depth%2 == 1:
                minimiseLayer()
uiElements = []
#Zeichnet alle Kreise
def drawField():
    for x in range(len(layers)):
        drawCircleLine(x,len(layers[x]))
posArray = []
#Zeichnet einen Reihe von Kreisen und speichert ihre Positionen in posArray ab.
def drawCircleLine(layerDepth, amountOfCircles):
    global cv
    global posArray
    posLineArray = []
    global width_Circle
    yPosTop = sizeY-offsetYToBorder - layerDepth*(circleCircleOffsetY+width_Circle)
    yPosBottom = yPosTop - width_Circle
    offsetBetweenCircles = calculateCircleCircleOffsetXInLayer(len(layers[layerDepth]))
    for x in range(amountOfCircles):
        xPosLeft = 0.5*offsetBetweenCircles+(x*(width_Circle+offsetBetweenCircles))
        xPosRight = xPosLeft+width_Circle
        posLineArray.append([xPosRight,xPosLeft,yPosTop,yPosBottom])
        id = cv.create_oval(xPosLeft,yPosTop,xPosRight,yPosBottom,width = 2)
        uiElements.append(id)
    posArray.append(posLineArray)
#Zeichnet eine Linie zwischen zwei Knoten unterschiedlicher Ebenen
def drawLine(parentPos,childPos,color):
    parentPosYBottom = parentPos[2]
    parentPosXMiddle = ((parentPos[0] + parentPos[1])/2)
    childPosYTop = childPos[3]
    childPosXMiddle = ((childPos[0] + childPos[1])/2)
    cv.create_line(childPosXMiddle,childPosYTop,parentPosXMiddle,parentPosYBottom, width = 2, fill = color)
#Zeichnet alle Linien zwischen den Knoten
def drawLines():
    global cv
    global posArray
    for y in range(len(posArray)-1):
        for x in range(len(posArray[y])):
            id = x
            parentX = math.ceil((id+1)/branching_factor)
            parentX-=1
            parentPos = posArray[(y+1)][parentX]
            childPos = posArray[y][x]
            drawLine(parentPos,childPos,"#030303")
#Zeichnet die entsprechenden Werte in die Knoten(Kreise)
def drawText():
    global cv
    for y in range(len(layers)):
        for x in range(len(layers[y])):
            middleX = (posArray[y][x][0] + posArray[y][x][1] ) /2
            middleY = (posArray[y][x][2] + posArray[y][x][3] ) /2
            cv.create_text(middleX,middleY,font=("Liberation Serif", int(width_Circle-((1/3.5)*width_Circle))),anchor= "center",text = str(layers[y][x]))
#Zeichnet die Linien, welche zum besten Ergebnis führen Rot
def drawSelectedLines():
    global cv
    global tree
    global posArray
    global depth
    curNode = None
    parentNode = None
    for n in (tree[::-1]):
        if n.parentNode[1] == depth:
            parentNode = n.parentNode
        if n.parentNode == parentNode:
            drawLine(posArray[parentNode[1]][parentNode[0]],posArray[n.childNode[1]][n.childNode[0]],"#EE6AA7")
            parentNode = n.childNode
            

generateNewOutcomes()
minimax()
drawField()
drawLines()
drawSelectedLines()
drawText()
root.mainloop()