#!/bin/bash

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

escolha = int(input("Digite o número correspondente à operação que deseja realizar para esses valores: soma (1), subtração (2), multiplicação (3) ou divisão (4):"))

if escolha == 1:
  soma = n1 + n2
  print('A soma dos números é:', soma)

elif escolha == 2:
  sub = n1 - n2
  print('A subtração de', n1, 'por', n2, 'é:', sub)

elif escolha == 3:
  mult = n1 * n2
  print('A multiplicação dos dois números é:', mult)

elif escolha == 4:
  div = n1 / n2
  print('A divisão de', n1, 'por', n2, 'é:', div)

else:
   print("Escolha inválida. Digite novamente.")

