from random import randint
itens = ('Pedra','Papel','Tesoura')

computador = randiant(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogdor = int(input('Qual é a sua jogada?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogdor]))
if computador == 0:  # Computador jogou Pedra
    if jogdor == 0:
        print('Empate!')
    elif jogdor == 1:
        print('Jogador venceu!')
    elif jogdor == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogdor == 0:
        print('Computador venceu!')
    elif jogdor == 1:
        print('Empate!')
    elif jogdor == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogdor == 0:
        print('Jogador venceu!')
    elif jogdor == 1:
        print('Computador venceu!')
    elif jogdor == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
elif computador == 3:
    if jogdor == 0:
        print('Jogador venceu!')
    elif jogdor == 1:
        print('Computador venceu!')
    elif jogdor == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida!')   