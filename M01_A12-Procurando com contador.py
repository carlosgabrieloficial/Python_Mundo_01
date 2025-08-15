#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que
#  posição ela aparece a primeira vez e em que posição ela aparece a última vez


frase = str(input('diga uma frase e ')).strip().upper()
n = frase.count('A')

print(f'a sua frase é :{frase}')

print(f'a letra escolhida aparece : {n} vezes')#CONTADOR DA LETRA 'A'

print(f'a primeira vez que aparece foi {frase.find('A')+1}')#LOCALINZADO A PRIMEIRA VEZ

print(f'e a ultima vez que aparece foi {frase.rfind('A')+1}')#LOCALINZADO A ULTIMA VEZ