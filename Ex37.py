numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('a conversão do numero para binário é {}'.format(bin(numero)[2:]))
elif opcao == 2:
    print('{} a conversão do numero para octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} a conversão do numero para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')