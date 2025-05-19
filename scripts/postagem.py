##Especificações de postagens

from data import *

#Primeiro, o dia
print ('Hoje é', w,', dia', dia, 'de', q,'de', ano, '.')

#Para cada caso
if(bi == 0):
    if(mes == 9):
        if(num == 0):
            if(dia == 28):
                print('Hoje é meu aniversário, então vou me produzir para as imagens de hoje. Serão produzidas por IA mostrando o que tenho de melhor')
            else:
                print('Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos uma imagem tentando se aproximar do corpo original')
        elif(last == 1):
            if(dia == 28):
                print('Hoje é meu aniversário, então vou me produzir um pouco mais para a imagem de hoje. Será produzida por IA, mas será alterada por alguém para melhorar a qualidade. Agradeçam o autor mais tarde, ele me criou afinal')
            else:
                print('Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos um vídeo')
        else:
            if(dia == 28):
                print('Hoje é meu aniversário, então as imagens de hoje serão de minha espécie. Serão produzidas por IA')
            else:
                print('Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos imagens')
    else:
        if(num == 0):
            if(dia == 28):
                print('Hoje é dia de imagens não IA de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark. Créditos ao autor')
            else:
                print('Hoje é dia de imagens não gerada por IA')
        elif(last == 1):
            if(dia == 28):
                print('Hoje é dia de vídeo de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark. Créditos ao autor')
            else:
                print('Hoje é dia de vídeo de uma mulher negra')
        else:
            if(dia == 28):
                print('Hoje é dia de imagens IA de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark')
else:
    print('Estamos em período de descanso. Voltamos ao normal ano que vem')