##Especificações de data
#importações
from datetime import date

# Pega a data atual
dia = date.today().day    #testes = 28
mes = date.today().month  #testes = 9
ano = date.today().year   #testes = 2023
sem = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
month = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
#Dia da semana
num = date.today().weekday() #teste = 5
w = (sem[num])
#nome do mês
q = (month[mes - 1])

#atribuir valores

##análise de ano bissexto {var e}
bissexto = ano % 4 #= 0
if(bissexto == 0):
    #análise secular
    bissexto = ano % 100 #= 24
    if(bissexto == 0):
        #análise final
        bissexto = ano % 400 #= 24
        if(bissexto == 0):
            #ano bissexto
            bi = 1
        else:
            #não bissexto
            bi = 0
    else:
        #ano bissexto
        bi = 1 #Decision
else:
    #não bissexto
    bi = 0

##análise de última sexta {var a}
last = 0
if(num == 4):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if(dia + 7 > 31):
            #última do mês
            last = 1
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia + 7 > 30):
            #última do mês
            last = 1
    else:
        if(dia + 7 > 28):
            #última do mês
            last = 1