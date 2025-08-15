#Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

#==============================================================
numero = int(input('diga um numero :'))
resultado = numero % 2
#==============================================================
if resultado == 1 :
    print(f'seu numero é {numero} e ele é impar')
#==============================================================
else :
    print(f'seu numero é {numero} e ele é par')
#==============================================================