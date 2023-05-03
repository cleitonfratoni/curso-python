"""
Iterando String com while
"""

#       123456789...
nome = 'Cleiton Fratoni' #Iteráveis
#          ...987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = f'*{nome[indice]}'
    novo_nome += letra
    indice += 1

novo_nome += '*'
print(novo_nome)