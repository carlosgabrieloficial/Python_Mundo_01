#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('diga o seu nome :')).strip().upper()
X = nome.split()

print(X)
print(X[0])
print(X[len(X)-1])