#Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada dos nomes

import random

nome1 = str(input('nome 1:'))
nome2 = str(input('nome 2:'))
nome3 = str(input('nome 3:'))
nome4 = str(input('nome 4:'))

lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)

print(f'a ordem da lista ficou :',{lista})
