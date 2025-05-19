###enhance
import random

from data import mes, dia

#mes
#dia
enhance = []
enhance.append("with")
biggy = ("big breasts", "big butt", "big hips")
bonus = ("and big nipples", "and open legs", "and big breasts", "big hips, big breasts and open legs")

maxr = 2
roll = random.randint(0,maxr)
if(mes == 9):
    if(dia == 28):
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
    maxr = 2
    roll = random.randint(0,maxr)
    if(roll == 2):
        enhance.append(bonus[1])
else:
    enhance.append(biggy[roll])
    maxr = 2
    roll = random.randint(0,maxr)
    if(roll == 2):
        enhance.append(bonus[0])

#print(' '.join(enhance))