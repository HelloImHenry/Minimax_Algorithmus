# Spielbaum Anzeigeprogramm
# Das Programm zeigt, wie der Minimax-Algorithmus den "besten" Zug aus einem bereits vorgegebenen Spielbaum ermittelt.
## Vorab:
### Die tiefste/unterste Ebene des Spielbaums wird in diesem Programm durch, Zufallszahlen, und nicht wie beim eigentlichen Minimax-Algorithmus durch, die möglichen Züge und jeweiligen rekursiven Reaktionen ermittelt.
## Wie das Programm genutzt wird:
### **Alle veränderbaren Variablen sind durch den Kommentar [VERÄNDERBAR] über der betreffenden Variable gekennzeichnet.**
### *__sizeX und sizeY__*: geben die Standardgröße des Fenster an. (Das Fenster vergrößert sich unter bestimmten Umständen um Text besser anzuzeigen.)
### *__branching_factor__*: gibt an wie viele Verzweigungen jeder Punkt des Spielbaums (außgeschlossen der Endknoten) besitzen soll.
### *__depth__*: gibt die Tiefe des Spielbaums an.
### *__colorMax__*: Die Farbe der Knoten welche die Werte aus ihren "Kindern" maximieren
### *__colorMin__*: Die Farbe der Knoten welche die Werte aus ihren "Kindern" minimieren
### *__colorSelected__*: Die Farbe der Verzweigung, welche der "Minimax-Algorithmus" ausgewählt hat.
## **Vorsicht mit den Werten.** Die Anzahl der Endknoten(= Tiefste Ebene)steigt durch den Faktor *depth^branching_factor*
