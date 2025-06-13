from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range (1,7+1):
    Ano = int(input('Em que ano a {}º nasceu? '.format(pessoas)))
    idade = ano_atual - Ano
if idade >= 21:
    totmaior += 1
else:
    totmenor += 1
print('Ao todo tivemos {} pessoas maior idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menor idade'.format(totmenor))
