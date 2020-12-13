# Geladene Bilder
bilder = []
img_aspect_ratio = 600.0/975.0

# Laden der Bilder in ein Array
def load_images():
    global bilder
    
    # 120 Bilder aus dem "data" Ordner laden
    for i in range(0, 120):
        if i < 10:
            bilder.append(loadImage("animation-00" + str(i) + ".jpg"))
        elif i < 100:
            bilder.append(loadImage("animation-0" + str(i) + ".jpg"))
        else:
            bilder.append(loadImage("animation-" + str(i) + ".jpg"))

# Korrektes Bild zeichnen
def draw_process(process, circle_diamater, window_size):
    
    # Image index berechnen
    img_idx = int(round((process)/3))
    
    # Rundungsproblem beheben
    if img_idx == 120:
        img_idx = 119
        
    # x Koordinate des Bildes berechnen: Fenstermitte minus 35 Prozent des Kreisdurchmessers   
    x_coord = window_size/2 - round(circle_diamater*0.35)
    
    # y Koordinate des Bildes berechnen: Fenstermitte minus 35 Prozent des Kreisdurchmessers, mal das Seitenverhaeltnis der Bilder
    y_coord = window_size/2 - round(circle_diamater*0.35)*img_aspect_ratio
    
    # Bildbreite berechnen: 70 Prozent des Kreisdurchmessers: Das Bild ist genau zentral im Fenster ausgerichtet
    img_width = round(circle_diamater*0.7)
    
    # Bildhoehe berechnen: 70 Prozent des Kreisdurchmessers, mal das Seitenverhaeltnis der Bilder
    img_height = round(circle_diamater*0.7)*img_aspect_ratio
    
    # Korrektes Bild zeichnen
    image(bilder[img_idx], x_coord, y_coord, img_width, img_height)
