
import random

nome1 = str(input('nome 1:'))
nome2 = str(input('nome 2:'))
nome3 = str(input('nome 3:'))
nome4 = str(input('nome 4:'))
lista = [nome1,nome2,nome3,nome4]
escolhe = random.choice(lista)

print(f'o nome escolhido é : {escolhe}')