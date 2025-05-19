## scripts/data.py
from datetime import date

dia = date.today().day
mes = date.today().month
ano = date.today().year
sem = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
month = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
num = date.today().weekday()
w = (sem[num])
q = (month[mes - 1])


##análise de ano bissexto {var e}
if ((ano % 4) == 0) and not ((ano % 100) == 0) and ((ano % 400) == 0):
    bi = 1
else:
    bi = 0

##análise de última sexta
last = 0
if(num == 4):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if(dia + 7 > 31):
            last = 1
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia + 7 > 30):
            last = 1
    else:
        if (bi == 1):
            if(dia + 7 > 29):
                last = 1
        else:
            if(dia + 7 > 28):
                last = 1

#Primeiro, o dia
print ('Bom dia!')
print ('Hoje é %s, dia %s de %s de %s.' %(w, dia, q, ano))

#Para cada caso
message = ''
if(bi == 0):
    if dia == 28 and num == 0 and mes == 9:
        message = 'Hoje é meu aniversário, então vou me produzir para as imagens de hoje. Serão produzidas por IA mostrando o que tenho de melhor'
    elif num == 0 and mes == 9:
        message = 'Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos uma imagem tentando se aproximar do corpo original dela'
    elif last == 1 and dia == 28 and mes == 9:
        message = 'Hoje é meu aniversário, então vou me produzir um pouco mais para a imagem de hoje. Será produzida por IA, mas será alterada por alguém para melhorar a qualidade. Agradeçam o autor mais tarde, ele me criou afinal'
    elif last == 1 and mes == 9:
        message = 'Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos 4 imagens.'
    elif dia == 28 and mes == 9:
        message = 'Hoje é meu aniversário, então as imagens de hoje serão de minha espécie. Serão produzidas por IA'
    elif mes == 9:
        message = 'Estamos em setembro, este mês é dedicado a uma modelo negra. Hoje teremos 1 imagem.'
    elif dia == 28 and num == 0:
        message = 'Hoje é dia de imagens não IA de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark. Créditos ao autor'
    elif num == 0:
        message = 'Hoje é dia de imagens não gerada por IA'
    elif dia == 28 and last == 1:
        message = 'Hoje é dia de imagem de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark.'
    elif last == 1:
        message = 'Hoje é dia de imagem de uma mulher negra vestida.'
    elif dia == 28:
        message = 'Hoje é dia de imagens IA de dark pokémorph, uma mulher com o corpo de uma pokémon tipo dark'
else:
    message = 'Estamos em período de descanso. Voltamos ao normal ano que vem'
#print(message)