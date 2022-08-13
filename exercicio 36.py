vcasa = float(input('Qual o valor da casa que você irá pagar? R$'))
vsalario = float(input('Informe o valor do seu salário mensal também: R$'))
vanos = int(input('Em quantos anos o senhor planeja pagar esta casa? '))

vtprest = vanos * 12
vtcasa = vcasa / vtprest
vsalario30 = vsalario * 0.3

if vtcasa <= vsalario30 :
    print(f'Seu empréstimo será aprovado e você pagará essa quantia R${vtcasa:.2f} por mês')
else: 
    print(f'Para pagar uma casa de R${vcasa} em {vanos} anos a prestação será de R${vtcasa:.2f}')
    print('EMPRÉSTIMO NEGADO!')