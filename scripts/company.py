###company
import random
#Estudar repetição do algoritmo, ele repete os mesmos valores
companion = []
members = ("man", "woman", "men", "women")
quantity = ("one", "two", "three", "four", "five")

maxr = 5
roll = random.randint(0,maxr)
mode = roll
#mode = 5
if(mode == 4):
    #with
    companion.append("with")
    maxr = 4
    roll = random.randint(1,maxr)
    companion.append(quantity[roll])
    if(roll >= 1):
        maxr = 3
        roll = random.randint(2,maxr)
        companion.append(members[roll])
    else:
        maxr = 1
        roll = random.randint(0,maxr)
        companion.append(members[roll])

#NOTA: orientação a objeto!
elif(mode == 5):
    #another [ebony][enhance][pose]
    companion.append("with another")
    #black = []
    ##Call ebony.py
    from ebony import *
    for x in range(len(nega)):
        companion.append(nega[x])
    #company.append(ebony)
    ##Call enhance.py
    from enhance import *
    for x in range(len(enhance)):
        companion.append(enhance[x])
    #company.append(enhance)
    ##Call pose.py
    from pose import *
    for x in range(len(pose)):
        companion.append(pose[x])
    #black.append(pose)
    #company.append(black)

#roll number from 0 to 2
##with
## number
#roll number from 1 to 5
#man/men
#woman/women
##other
## reroll [ebony][enhance][pose]
#print(' '.join(companion))