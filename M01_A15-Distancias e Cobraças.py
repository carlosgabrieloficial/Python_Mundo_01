#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('digame qual foi a distancia da viagem ?'))

if distancia <= 200 :
    valor1 = (distancia*0.45)
    print(f'Sua distancia é menor que 200')
    
else:
    valor2 = (distancia*0.50)
    print(valor2)

print('===fim===')