""" Caculadora com While """
while True: # Repetição da Calculadora
    numero1 = input('Digite o 1º número: ') # Recebe o primeiro numero
    numero2 = input('Digite o 2º número: ') # Recebe o segundo numro
    operador = input('Digite o operador (+-*/): ') # Recebe o operador
    
    numero_validos = None # flag para validar os numeros
    num_1_float = 0
    num_2_float = 0
    
    try: # validando os numeros
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numero_validos = True # numeros validados
    except:
        numero_validos = None
        
    if numero_validos is None: # numero(s) invalidos
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-*/' # range de operadores validos
    
    if operador not in operadores_permitidos: # validando operadores
        print('Operdor inválido.')
        continue
    
    if len(operador) > 1: # validando quantidade de operadores
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo.')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    else:
        print('Nunca deveria chegar aqui.')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s') # lower converte tudo de maiúsculo para minúscula. 'startswitch' começa com.
    if sair is True: # fim do programa
        break