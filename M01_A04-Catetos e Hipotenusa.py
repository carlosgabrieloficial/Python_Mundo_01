# Faça um programa que leia o comprimento
# cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

ca = float(input('ca :'))
co = float(input('co :'))
#hi = ((ca**2 + co**2) **(1/2)) versao mais trabalhosa
hi = math.hypot(co,ca)
print(f'a sua hipotenusa é {hi}')
