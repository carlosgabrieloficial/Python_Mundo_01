#Crie um programa que leia
# o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
#===============================================================================
cidade = str(input('diga qual o nome da sua cidade ?')).strip()
#===============================================================================
print(f'O nome da sua cidade é {cidade}')
print (cidade[:5].upper() == 'SANTO')
#===============================================================================
