# Spielbaum Anzeigeprogramm
# Das Programm zeigt, wie der Minimax-Algorithmus den "besten" Zug aus einem bereits vorgegebenen Spielbaum ermittelt.
## Vorab:
### Die tiefste/unterste Ebene des Spielbaums wird in diesem Programm, durch Zufallszahlen, und nicht wie beim eigentlichen Minimax-Algorithmus durch die möglichen Züge, ermittelt.
## Wie das Programm genutzt wird:
### **Alle Variablen die veränderbar sind, sind durch den Kommentar [Veränderbar] über der betreffenden Variable gekennzeichnet.**
### *sizeX und sizeY* geben die Standardgröße des Fenster an. (Das Fenster vergrößert sich unter bestimmten Umständen um Text besser anzuzeigen.)
### *branching_factor* gibt an wie viele Verzweigungen jeder Punkt des Spielbaums (natürlich ausgeschloßen der letzen Reihe) besitzen soll.
### *depth* gibt die Tiefe des Spielbaums an.
### **Vorsicht mit den Werten.** Wenn die die Anzahl der Punkte steigt durch den Faktor *depth^branching_factor*
