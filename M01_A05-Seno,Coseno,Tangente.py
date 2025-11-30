# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("escolha entre 30, 45 ,60 :"))
seno = math.sin(math.radians(angulo))
cosn = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print ('o seu seno é : {:.2f},\no seu cosceno é : {:.2f} ,\nlogo a sua tangente é : {:.2f}'.format(seno, cosn, tang))