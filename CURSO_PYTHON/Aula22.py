# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo no que é
# usado para representar um valor

# entrada = (input('[E]ntrar [S]air: '))

# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# #if True:
# # ...
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avalaiação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)