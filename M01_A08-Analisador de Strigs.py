nome = str(input('diga o seu nome :'))

print(f'O seu o nome é {nome},\n o seu nome com todas as letras maiusculas é assim : {nome.upper()}')
print(f'O seu o nome com todas as as letras minisculas é : {nome.lower()}')

print(f'o seu nome tem esse numero de caracteres : {(len(nome))}')
print(f'agora desconsiderando os espaços eles tem esse numero : {(len(nome)) - nome.count(' ')}')

separar = nome.split()
print(f'O seu primeiro nome é: {separar[0]}, e ele tem {(len(separar[0]))} letras')