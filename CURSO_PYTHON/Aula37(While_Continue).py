"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Não vou mostra o', contador)
        continue #pula o laço de repetição
    if contador >= 10 and contador <=20:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break #para o laço de repetição
    
print('Acabou')