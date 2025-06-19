
quantidade = soma = maiorvalor = menorvalor = media = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maiorvalor = menorvalor = num
    else:
        if num > maiorvalor:
            maiorvalor = num
        if num < menorvalor:
            menorvalor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quantidade
print('Você digitou {} números e a média entre eles foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maiorvalor, menorvalor))