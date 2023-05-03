"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero: ')
numero_par_impar = None
if numero.isdigit():
    numero_par_impar = int(numero) % 2
    if numero_par_impar == 1:
        print('Este é um numero impar.')
    else:
        print('Este é um numero par.')
else:
    print('O numero digitado é invalido. Favor digite um numero inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Favor digite que horas são: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')
except:
    print('Por favor, digite um números inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome >=1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite mais de uma letra.')