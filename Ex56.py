totmulher = 0
maioridade = 0
menoridade = 0
somaidade = 0
mediaidade = 0
for p in range (1,5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if idade == 1:
        maioridade = idade
        menoridade = idade
    else:
        if idade > maioridade:
            maioridade = idade
        if idade < menoridade:
            menoridade = idade
    if sexo == 'F' and 'f' and idade < 20:
        totmulher += 1
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
