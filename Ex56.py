totmulher = 0 #total de mulheres com menos de 20 anos
maioridade = 0 #maior idade do grupo
menoridade = 0 #menor idade do grupo
somaidade = 0 #soma das idades do grupo
mediaidade = 0 #média de idade do grupo
maioridadehomem = 0 #maior idade entre os homens
nomevelho = '' #nome do homem mais velho
for p in range (1,5):
    print('----- {}ª pessoa -----'.format(p))   
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade == 1:
        maioridade = idade
        menoridade = idade
    else:
        if idade > maioridade:
            maioridade = idade
        if idade < menoridade:
            menoridade = idade
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
