soma = 0 #armazena o número que for divisível por 2
for Pergunta in range (1,7):
    PerNum = int(input("Digite um número: "))
    if PerNum % 2 == 0:
        soma += PerNum
print('A soma dos números pares é: {}'.format(soma))