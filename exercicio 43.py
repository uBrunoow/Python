peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso / (altura ** 2)

if imc < 18.5: 
    print (f'Seu IMC é de {imc:.1f} \n Você está ABAIXO do peso normal')

elif 18.5 <= imc < 25: 
    print (f'Seu IMC é de {imc:.1f} \n Você está no PESO ideal')

elif 25 <= imc < 30: 
    print (f'Seu IMC é de {imc:.1f} \n Você está no SOBREPESO')

elif 30 <= imc < 40: 
    print (f'Seu IMC é de {imc:.1f} \n Você está com OBESIDADE')

else: 
    print (f'Seu IMC é de {imc:.1f} \n Você está com OBESIDADE MÓRBIDA, cuidado!')