from datetime import date

atual = date.today().year
nasc= int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:  
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(18 - idade))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))