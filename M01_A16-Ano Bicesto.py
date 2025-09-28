
ano = int(input('qual é o ano em questao ?'))

if ano % 4== 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'esse ano de {ano} é bi')
else:
    print(f'esse ano {ano}, nao é bi')
