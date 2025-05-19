import random as r
from data import mes, dia


power = 5
nega = []
model = "black woman"
poke = ("Umbreon", "Murkrow", "Sneasel", "Houndour", "Houndoom", "Tyranitar", "Poochyena", "Mightyena", "Nuzleaf", "Shiftry", "Sableye", "Carvanha", "Sharpedo", "Cacturne", "Crawdaunt", "Absol", "Honchkrow", "Stunky", "Skuntank", "Spiritomb", "Drapion", "Weavile", "Darkrai", "Purrloin", "Liepard", "Sandile", "Krokorok", "Krookodile", "Scraggy", "Scrafty", "Zorua", "Zoroark", "Pawniard", "Bisharp", "Vullaby", "Mandybuzz", "Deino", "Zweilous", "Hydreigon", "Greninja", "Pangoro", "Inkay", "Malamar", "Yveltal", "Hoopa", "Incineroar", "Guzzlord")

##ebony
#if(dia == 28):
roll = r.randint(0,1)
mode = roll
if(mode == 1):
    company = ()
    roll = r.randint(0,len(poke) - 1)
    choice = roll
    if(choice == 4 or choice == 5 or choice == 10 or choice == 12 or choice == 15):
        maxr = 5
        roll = r.randint(0,maxr)
        power = roll
        power = 5
        if(power == 5):
            nega.append("Mega")
    nega.append(poke[choice])

else:
    nega.append(model)

#print(' '.join(negra))


##enhance
enhance = ["with"]
biggy = ("big breasts", "big butt", "big hips")
bonus = ("and big nipples", "and open legs", "and big breasts", "big hips, big breasts and open legs")

roll = r.randint(0,len(biggy) - 1)
if mes == 9 and dia == 28:
        roll = 2
more = roll
if(more == 2):
    if(mes == 9 and dia == 28):
            enhance.append(bonus[3])
    else:
        enhance.append(biggy[roll])
        enhance.append(bonus[2])
elif(more == 1):
    enhance.append(biggy[roll])
    roll = r.randint(0,len(biggy) - 1)
    if(roll == 2):
        enhance.append(bonus[1])
else:
    enhance.append(biggy[roll])
    roll = r.randint(0,len(biggy) - 1)
    if(roll == 2):
        enhance.append(bonus[0])

#print(' '.join(enhance))

###pose
pose = []
action = ("dancing", "posing", "walking", "strolling", "sitting", "laying down", "smooching", "hugging", "looking at viewer", "looking away", "looking back", "backwiew")

roll = r.randint(0,len(action) - 1)
pose.append(action[roll])
#print(' '.join(pose))

###company
#Estudar repetição do algoritmo, ele repete os mesmos valores
companion = []
members = ("man", "woman", "men", "women")
quantity = ("one", "two", "three", "four", "five")

roll = r.randint(0,5)
mode = roll
#mode = 5
if(mode == 4):
    #with
    companion.append("with")
    roll = r.randint(1,len(quantity) - 1)
    companion.append(quantity[roll])
    if(roll >= 1):
        roll = r.randint(2,len(members) - 1)
        companion.append(members[roll])
    else:
        maxr = 1
        roll = r.randint(0,len(members) - 2)
        companion.append(members[roll])

#NOTA: orientação a objeto!
elif(mode == 5):
    #another [ebony][enhance][pose]
    companion.append("with another")
    for x in range(len(nega)):
        companion.append(nega[x])
    for x in range(len(enhance)):
        companion.append(enhance[x])
    for x in range(len(pose)):
        companion.append(pose[x])
#print(' '.join(companion))

###place
place = []
house = ("bedroom", "bathroom", "kitchen", "garden", "garage", "swimming pool", "attic", "balcony", "staircase")
private = ("bitcoin bank", "bank", "supermarket", "night club", "school", "mall", "hospital", "cafe", "library", "farm", "castle", "dojo", "hot spring")
public = ("park", "beach", "alleyway", "market", "street", "bridge", "parking lot", "car", "train station", "train", "bus stop", "bus", "pier", "boat", "forest", "lake", "waterfall", "sewers", "river", "volcano", "cavern", "space")
vowel = ("at an", "at a")

roll = r.randint(0,2)
mode = roll
if(mode == 0):#house
    roll = r.randint(0,len(house) - 1)
    if(roll == 6):
        place.append(vowel[0])
    else:
        place.append(vowel[1])
    place.append(house[roll])

elif(mode == 1):#private
    roll = r.randint(0,len(private) - 1)
    place.append(vowel[1])
    if(roll == 0):
        company = ()
    place.append(private[roll])

else:#public
    roll = r.randint(0,len(public) - 1)
    if(roll == 2):
        place.append(vowel[0])
    else:
        place.append(vowel[1])
    place.append(public[roll])

###extra
extra = []
time = ("daytime", "nightime")
weather = ("sunny", "rainy", "snowy", "overcast", "foggy", "stormy")
skinEnhance = ("darker skin", "blue light", "yellow light", "green light", "red light", "orange light", "purple light")
hairStyle = ("afro hair", "straight hair", "wavy hair", "curly hair", "ponytail")

maxr = 2
roll = r.randint(0,maxr)
bon = roll
if(bon >=1):
        extra = [","]
        roll = r.randint(0,len(time) - 1)
        extra.append(time[roll])
        
        roll = r.randint(0,len(weather) - 1)
        extra.append(weather[roll])
        if(bon == 2):
            extra = [","]
            roll = r.randint(0,len(skinEnhance) - 1)
            extra.append(skinEnhance[roll])

            extra = [","]
            roll = r.randint(0,len(hairStyle) - 1)
            extra.append(hairStyle[roll])
        
###style
style = []
drawing = ["sketch", "aquarella", "digital"]
photograph = ["realistic", "futuristic", "romantic"]
furryArt =["cartoon", "comic"]
artist = ["art by MLeonHeart", "art by Whisperfoot", "art by R-MK", "art by Drakeraynier", "art by CoolieHigh", "art by Saintversa", "art by Lyorenth", "art by Ashraely", "art by Miso_Souperstar", "art by Sususuigi", "art by Latiar", "art by LiveForTheFunk", "art by SligarTheTiger", "art by Lysergyde", "art by Viejillox", "art by DimWitDog, art by Atherol", "art by Borky_draws", "art by Capaoculta"]
vintage = ["old-fashion", "classic", "country style"]
colourControl = ["sepia", "black and white", "saturated"]

maxr = 2
roll = r.randint(0,maxr)
mode = roll
if(mode ==1):
    style = [","]
    maxr = 4
    roll = r.randint(0,maxr)
    choice = roll
    if(choice == 0):
        roll = r.randint(0,len(drawing) - 1)
        style.append(drawing[roll])
    if(choice == 1):
        roll = r.randint(0,len(photograph) - 1)
        style.append(photograph[roll])
    if(choice == 2):
        roll = r.randint(0,len(furryArt))
        art = roll
        if(art == 2):
            roll = r.randint(0,len(artist) - 1)
            furryArt.append(artist[roll])
        style.append(furryArt[art])
    if(choice == 3):
        roll = r.randint(0,len(vintage) - 1)
        style.append(vintage[roll])
    if(choice == 4):
        roll = r.randint(0,len(colourControl) - 1)
        style.append(colourControl[roll])
elif(mode ==2):
    style = [","]  
    maxr = 1
    roll = r.randint(0,maxr)
    choice = roll
    if(choice == 0):
        roll = r.randint(0,len(photograph) - 1)
        style.append(photograph[roll])
        
        roll = r.randint(0,len(drawing) - 1)
        style.append(drawing[roll])
        
        roll = r.randint(0,len(furryArt))
        art = roll
        if(art == 2):
            roll = r.randint(0,len(artist) - 1)
            furryArt.append(artist[roll])
        style.append(furryArt[art])
    if(choice == 1):
        roll = r.randint(0,len(vintage) - 1)
        style.append(vintage[roll])
        
        roll = r.randint(0,len(colourControl) - 1)
        style.append(colourControl[roll])
