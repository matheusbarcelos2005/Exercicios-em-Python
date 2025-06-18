num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

while (1,5):
    print(''' [1] Somar
 [2] Multiplicar
 [3] Maior)
 [4] Novos números
 [5] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}.'.format(num1, num2, soma))
    elif opcao == 2:
        multipli = num1 * num2
        print('A multiplicação entre {} e {} é {}.'.format(num1, num2, multipli))
    elif opcao == 3:
        if num1 > num2:
            print('O maior valor é {}.'.format(num1))
        else:
            print('O maior valor é {}.'.format(num2))
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida. Tente novamente.')