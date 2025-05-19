###extra
import random

extra = []
time = ("daytime", "nightime")
weather = ("sunny", "rainy", "snowy", "overcast", "foggy", "stormy")
skinEnhance = ("darker skin", "blue light", "yellow light", "green light", "red light", "orange light", "purple light")
hairStyle = ("afro hair", "straight hair", "wavy hair", "curly hair", "ponytail")

maxr = 2
roll = random.randint(0,maxr)
bon = roll
if(bon >=1):
        extra = [","]
        maxr = 1
        roll = random.randint(0,maxr)
        extra.append(time[roll])
        
        maxr = 5
        roll = random.randint(0,maxr)
        extra.append(weather[roll])
        if(bon == 2):
            extra = [","]
            maxr = 6
            roll = random.randint(0,maxr)
            extra.append(skinEnhance[roll])

            extra = [","]
            maxr = 4
            roll = random.randint(0,maxr)
            extra.append(hairStyle[roll])
        