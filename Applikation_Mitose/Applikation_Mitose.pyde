import math
from draw_process import *
process_angle = 0.0
circle_diamater = 800
window_size = 1200

def setup():
    # Frequenz der Anwendung
    frameRate(24)
    # Rechteckiges Fenster
    size(window_size, window_size)
    # Den Text vom Mittelpunkt aus zeichnen
    textAlign(CENTER)
    # Die Bilder in den Arbeitsspeicher laden.
    load_images()

def draw():
    # Hintergrund
    background(255)
    # Ruler zeichnen (Quelle: Noa Sendlhofer)
    draw_ruler()
    # Korrektes Bild zum Prozess zeichnen
    draw_process(round(process_angle), circle_diamater, window_size)
    # Prozessbezeichnungen zeichnen
    draw_descriptions()
    
def draw_descriptions():
    # Distanz der äusseren Kreise zum Fenstermittelpunkt
    distance = circle_diamater/2 + 100
    # Winkel zwischen den Kreisen
    angle = 360.0/7.0
    # Kein schwarzer Rand bei den Kreisen
    noStroke()
    # Textgrösse in den Kreisen
    textSize(25)
    
    # Den richtigen Namen, zu den Phasennummern wählen
    Process_Names = ["Mutterzelle", "Interphase", "Prophase", "Metaphase", "Anaphase", "Telophase", "Cytokinese"]
    
    # Für jeden der sieben Kreise wiederholen
    for i in range(0, 7):
        # Die x Koordinate berechnen mit dem Kosinus, multipliziert mit der Distanz zum Fenstermittelpunkt (Quelle: Noa Sendlhofer)
        x = window_size/2 + (cos(math.radians(angle*i - 90))*distance)
        # Die y Koordinate berechnen mit dem Sinus, multipliziert mit der Distanz zum Fenstermittelpunkt (Quelle: Noa Sendlhofer)
        y = window_size/2 + (sin(math.radians(angle*i - 90))*distance)
        # Die Kreise mit blauer Farbe füllen
        fill(0,150,255)
        # Die Kreise an den berechneten Koordinaten zeichnen
        circle(x, y, 140)
        # Den Text schwarz zeichnen
        fill(0,0,0)
        # Den richtigen Namen, zu den Phasennummern wählen
        text(Process_Names[i], x, y + 10)
    
    # Den schwarzen Rand wieder aktivieren
    stroke(0,0,0)
    # Das füllen von Zeichnungen deaktiviern
    noFill()
    
    
#Quelle gesamte Funktion: Noa Sendlhofer  
def draw_ruler():
    global process_angle
       
    #Kreis zeichnen
    strokeWeight(4)
    circle(window_size/2, window_size/2, circle_diamater)
    
    #Punkt zeichnen nach Prozess Winkel
    strokeWeight(50)
    
    # Wir zeichnen den Punkt des Rulers am korrekten Ort zum Prozesswinkel.
    # Um die richtigen Koordinaten zu erhalten, müssen wir von unserem Winkel jeweils 90 Grad subtrahieren. Dies stammt daher, dass der Einheitskreis bei 90 Grad beginnt. 
    # Alle Positionen wären somit um 90 Grad verschoben.
    point(window_size/2+math.cos(math.radians(process_angle - 90))*(circle_diamater/2), window_size/2 + math.sin(math.radians(process_angle - 90))*(circle_diamater/2))
    
    # Hypothenuse berechnen mit Pythagoras
    H = math.sqrt(abs(window_size/2 - mouseX)**2 + abs(window_size/2 - mouseY)**2)
    
    # Checken, ob die Maus innerhalb von +- 100 Pixel des Kreises ist
    if H < circle_diamater/2 + 100 and H > circle_diamater/2 - 100 and mousePressed == True:
        
        # Winkel anpassen, fall die Maus in der oberen respektive underen Hälfte des Kreises ist.
        if mouseY < window_size/2:
            
            # Szenario 1, Wir befinden uns im ersten Quadranten des Einheitskreises:
            # Um den korrekten Winkel zu erhalten müssen wir hier nur 90 Grad minus den Winkel des Arkuskosinus rechnen.
            
            if mouseX > window_size/2:
                process_angle = 90 - math.degrees(math.acos((mouseX - window_size/2)/H))
                          
            # Szenario 2, wir befinden uns im zweiten Quadranten des Einheitskreises:
            # Hier müssen wir 450 Grad minus den Winkel des Arkuskosinus rechnen.
            
            else:
                process_angle = 450 - math.degrees(math.acos((mouseX - window_size/2)/H))
         
        # Szenario 3, wir befinden uns im dritten oder vierten Quadranten des Einheitskreises:
        # Hier müssen wir nur 90 Grad plus den Winkel des Arkuskosinus rechnen.
        
        else:
            process_angle = 90 + math.degrees(math.acos((mouseX - window_size/2)/H))
