# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
#=================================================================================
numero = int(input('diga um numero de ate 4 digitos :'))
#=================================================================================
#aqui separa as unidades/dezenas/centenas/milhares 
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
#=================================================================================
#aqui vai ser area daquilo que eu quero mostrar
#=================================================================================
print(f'a sua unid é: {u}')
print(f'a sua deze é: {d}')
print(f'a sua cent é: {c}')
print(f'e seu mil  é: {m}')
#=================================================================================