""" 
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'cleiton Fratoni'
outra_variavel = f'{string[:6]}ABC{string[7:]}'

print(string)
print(outra_variavel)
print(string.capitalize	()) #capitalize deixa a primera letra em maiúsculo ou minusculo
print(string.zfill(100))