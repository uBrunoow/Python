ano = int(input('Ano de nascimento: '))

alist = 2022 - ano 

if alist < 18:
    alist2 = 18 - alist 
    ano2 = 2022 + alist2
    print (f' Para quem nasceu em {ano} tem {alist} anos em 2022 \n Ainda faltam {alist2} anos para o alistamento \n Seu alistamento será em {ano2} . ')

elif alist == 18:
    print (f' Você nasceu em {ano} tem {alist} em 2022 \n Você tem que se alistar IMEDIATAMENTE! ')

else: 
   alist3 = alist - 18
   ano3 = 2022 - alist3
   
   print (f' VocÊ nasceu em {ano} tem {alist} em 2022 \n Você deveria ter se alistado a {alist3} \n Seu alistamento foi em {ano3}')