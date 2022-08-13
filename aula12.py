nome = str(input('Qual é o seu nome?'))

if nome == 'Bruno':
    print ('Que nome bonito')

elif nome == 'Betina' or nome == 'Adriana' or nome == 'Rafael':
    print ('Seu nome é bem popular aqui no Brasil!')

else: 
    print ('Seu nome é bem normal...')

print (f'Tenha um bom dia, {nome}!')