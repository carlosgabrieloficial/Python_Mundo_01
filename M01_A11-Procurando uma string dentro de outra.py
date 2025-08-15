#Crie um programa que leia o
# nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('diga o seu nome')).strip()

print(f'nome e {nome}')
print('seu nome tem silva ? {}'.format('silva' in nome.lower()))

