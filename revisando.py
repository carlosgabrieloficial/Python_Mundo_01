# numero = int(input("Digite um numero :"))
# salarioAtual = numero + (numero*0.15)

# print(f"{salarioAtual}")
#=======================================================================

# import math

# numero = float(input("Digite um numero"))
# raiz = math.sqrt(numero)

# print(f"{raiz}")
#=======================================================================

# import math 

# angulo = float(input('Escolha um numero entre [30,45,60]'))

# seno = math.sin(math.radians(angulo))
# coseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))

# print(seno)
# print(coseno)
# print(tangente)

#=======================================================================


# import random 

# def lista():

#     print("===LISTA DE NOMES ===")
#     listaNomes =[]
#     for i in range(0,5):
#         nome = str(input(f"Nome{i+1}"))
#         listaNomes.append(nome)

#     print("PRONTO")

#     escolha = random.choice(listaNomes)
#     print(f"o nome escolhindo foi {escolha}", end=" ")

#     print(listaNomes)


# lista()

#=======================================================================

# from random import shuffle


# def nomeAlunos ():

#     listaAlunos = []

#     for i in range(0,4):

#         aluno = str(input(f"Aluno {i}"))
#         listaAlunos.append(aluno)

#     shuffle(listaAlunos)
#     return listaAlunos

# alunos_embaralhados = nomeAlunos()
# print("--- ORDEM --- ")
# for aluno in alunos_embaralhados:
#     print(f"{aluno}\n", end="")