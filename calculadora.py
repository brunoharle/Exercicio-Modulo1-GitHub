num = 0
escolha = 0
lista = []

while num < 999:
  num = int(input('Digite os números que deseja inserir na calculadora \n'
                  'Após digite "999" para escolher a operação desejada \n'))
  print('\n-------------- \n')

  if num != 999:
    lista.append(num)

print('\n-------------- \n')
print('Números inseridos:', lista)
print('\n-------------- \n')

while escolha <= 4:

  # Menu de Operações
  print('Escolha a operação:')
  print('1. Adição')
  print('2. Subtração')
  print('3. Multiplicação')
  print('4. Divisão')
  print('999. Sair \n')

  print('-------------- \n')

  # Entrada do usuário
  escolha = int(input('Digite a operação desejada '))

  print('\n-------------- \n')

  # Verifica se a entrada é válida
  if escolha in (1, 2, 3 , 4):

    if escolha == 1:
      soma = 0
      for val in lista:
        soma += val
      print('A soma dos números é igual a:', soma)
      print('\n-------------- \n')

    if escolha == 2:
      sub = lista[0]
      for val in lista[1:]:
        sub -= val
      print('A subtração dos números é igual a:', sub)
      print('\n-------------- \n')

    if escolha == 3:
      mult = 1
      for val in lista:
        mult *= val
      print('A multiplicação dos números é igual a:', mult)
      print('\n-------------- \n')

    if escolha == 4:
      div = lista[0]
      for val in lista[1:]:
        if val == 0:
          print('Erro: Divisão por 0 não existe')
        div /= val
      print('A divisão dos números é igual a:', div)
      print('\n-------------- \n')

  elif escolha == 999:
    print('Você saiu!')
    break
