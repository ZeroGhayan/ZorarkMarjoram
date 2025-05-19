###place
import random

place = []
house = ("bedroom", "bathroom", "kitchen", "garden", "garage", "swimming pool", "attic", "balcony", "staircase")
private = ("bitcoin bank", "bank", "supermarket", "night club", "school", "mall", "hospital", "cafe", "library", "farm", "castle", "dojo", "hot spring")
public = ("park", "beach", "alleyway", "market", "street", "bridge", "parking lot", "car", "train station", "train", "bus stop", "bus", "pier", "boat", "forest", "lake", "waterfall", "sewers", "river", "volcano", "cavern", "space")
vowel = ("at an", "at a")

maxr = 2
roll = random.randint(0,maxr)
mode = roll
if(mode == 0):#house
    maxr = 8
    roll = random.randint(0,maxr)
    if(roll == 6):
        place.append(vowel[0])
    else:
        place.append(vowel[1])
    place.append(house[roll])

elif(mode == 1):#private
    maxr = 8
    roll = random.randint(0,maxr)
    place.append(vowel[1])
    if(roll == 0):
        company = ()
    place.append(private[roll])

else:#public
    maxr = 8
    roll = random.randint(0,maxr)
    if(roll == 2):
        place.append(vowel[0])
    else:
        place.append(vowel[1])
    place.append(public[roll])