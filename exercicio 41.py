ano = int(input('Ano de nascimento: '))
idade = 2022 - ano 

if idade <= 9:
    print (f'VocÊ tem {idade} anos. \n Classificação MIRIM!  ')

elif idade <= 14:
    print (f'VocÊ tem {idade} anos. \n Classificação INFANTIL!  ')

elif idade <= 19:
    print (f'VocÊ tem {idade} anos. \n Classificação JUNIOR!  ')

elif idade <= 25:
    print (f'VocÊ tem {idade} anos. \n Classificação SÊNIOR!  ')

else: 
    print (f'Você tem {idade} anos. \n Classificação MASTER! ')