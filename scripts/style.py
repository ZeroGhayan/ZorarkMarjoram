###style
import random
style = []
drawing = ["sketch", "aquarella", "digital"]
photograph = ["realistic", "futuristic", "romantic"]
furryArt =["cartoon", "comic"]
artist = ["art by MLeonHeart", "art by Whisperfoot", "art by R-MK", "art by Drakeraynier", "art by CoolieHigh", "art by Saintversa", "art by Lyorenth", "art by Ashraely", "art by Miso_Souperstar", "art by Sususuigi", "art by Latiar", "art by LiveForTheFunk", "art by SligarTheTiger", "art by Lysergyde", "art by Viejillox", "art by DimWitDog, art by Atherol", "art by Borky_draws", "art by Capaoculta"]
vintage = ["old-fashion", "classic", "country style"]
colourControl = ["sepia", "black and white", "saturated"]

maxr = 2
roll = random.randint(0,maxr)
mode = roll
if(mode ==1):
    style = [","]
    maxr = 4
    roll = random.randint(0,maxr)
    choice = roll
    if(choice == 0):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(drawing[roll])
    if(choice == 1):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(photograph[roll])
    if(choice == 2):
        maxr = 2
        roll = random.randint(0,maxr)
        art = roll
        if(art == 2):
            maxr = 18
            roll = random.randint(0,maxr)
            furryArt.append(artist[roll])
        style.append(furryArt[art])
    if(choice == 3):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(vintage[roll])
    if(choice == 4):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(colourControl[roll])
elif(mode ==2):
    style = [","]  
    maxr = 1
    roll = random.randint(0,maxr)
    choice = roll
    if(choice == 0):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(photograph[roll])
        
        roll = random.randint(0,maxr)
        style.append(drawing[roll])
        
        roll = random.randint(0,maxr)
        art = roll
        if(roll == 2):
            maxr = 18
            roll = random.randint(0,maxr)
            furryArt.append(artist[roll])
        style.append(furryArt[art])
    if(choice == 1):
        maxr = 2
        roll = random.randint(0,maxr)
        style.append(vintage[roll])
        
        roll = random.randint(0,maxr)
        style.append(colourControl[roll])