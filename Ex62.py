primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10  # Inicializa com 10 termos
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais  =  int (input('Quantos termos você quer mostrar a mais? '))
print('Fim.')
print('Progressão finalizada com {} termos mostrados.'.format(total))
