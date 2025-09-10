# Calculadora simples que realiza soma, subtração, multiplicação ou divisão com base na escolha do usuário.
# A escolha dos números a serem operados e da operação é feita via input do usuário.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

# A escolha da operação é feita via input do usuário.
escolha = int(input("Digite o número correspondente à operação que deseja realizar para esses valores: soma (1), subtração (2), multiplicação (3) ou divisão (4):"))

# Estrutura condicional para realizar a operação escolhida.
# Soma:
if escolha == 1:
  soma = n1 + n2
  print('A soma dos números é:', soma)

# Subtração:
elif escolha == 2:
  sub = n1 - n2
  print('A subtração de', n1, 'por', n2, 'é:', sub)

# Multiplicação:
elif escolha == 3:
  mult = n1 * n2
  print('A multiplicação dos dois números é:', mult)

# Divisão:
elif escolha == 4:
  div = n1 / n2
  print('A divisão de', n1, 'por', n2, 'é:', div)

# Caso a escolha seja inválida:
else:
   print("Escolha inválida. Digite novamente.")

# Para executar o script, use o comando:
chmod +x calculadora.sh
