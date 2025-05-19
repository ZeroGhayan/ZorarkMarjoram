###ebony
import random
from data import dia
from enhance import enhance
#class nega():
#def nega():
#dia = 28
power = 5
nega = []
model = ("black woman","black women")
#poke = ["Umbreon", "Murkrow", "Sneasel", "Houndour", "Houndoom", "Mega Houndoom", "Tyranitar", "Mega Tyranitar", "Poochyena", "Mightyena", "Nuzleaf", "Shiftry", "Sableye", "Mega Sableye", "Carvanha", "Sharpedo", "Mega Sharpedo", "Cacturne", "Crawdaunt", "Absol", "Mega Absol", "Honchkrow", "Stunky", "Skuntank", "Spiritomb", "Drapion", "Weavile", "Darkrai", "Purrloin", "Liepard", "Sandile", "Krokorok", "Krookodile", "Scraggy", "Scrafty", "Zorua", "Zoroark", "Pawniard", "Bisharp", "Vullaby", "Mandybuzz", "Deino", "Zweilous", "Hydreigon", "Greninja", "Pangoro", "Inkay", "Malamar", "Yveltal", "Hoopa", "Incineroar", "Guzzlord"]
##Para caso use o comentado abaixo
poke = ("Umbreon", "Murkrow", "Sneasel", "Houndour", "Houndoom", "Tyranitar", "Poochyena", "Mightyena", "Nuzleaf", "Shiftry", "Sableye", "Carvanha", "Sharpedo", "Cacturne", "Crawdaunt", "Absol", "Honchkrow", "Stunky", "Skuntank", "Spiritomb", "Drapion", "Weavile", "Darkrai", "Purrloin", "Liepard", "Sandile", "Krokorok", "Krookodile", "Scraggy", "Scrafty", "Zorua", "Zoroark", "Pawniard", "Bisharp", "Vullaby", "Mandybuzz", "Deino", "Zweilous", "Hydreigon", "Greninja", "Pangoro", "Inkay", "Malamar", "Yveltal", "Hoopa", "Incineroar", "Guzzlord")

maxr = 1
roll = random.randint(0,maxr)
mode = roll
if(dia == 28):
    mode = 2
if(mode == 2):
    company = ()
    maxr = 46 #46 for non mega, 51 for mega
    roll = random.randint(0,maxr)
    choice = roll
    if(choice == 4 or choice == 5 or choice == 10 or choice == 12 or choice == 15):
        maxr = 5
        roll = random.randint(0,maxr)
        power = roll
        power = 5
        if(power == 5):
            nega.append("Mega")
    nega.append(poke[choice])

else:
    nega.append(model[roll])

#print(' '.join(nega))