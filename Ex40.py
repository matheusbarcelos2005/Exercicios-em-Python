Nota1 = float(input('Digite sua primeira nota: '))
Nota2 = float(input('Digite sua segunda nota: '))

Media = (Nota1 + Nota2) / 2

if Media <5:
    print('Aluno reprovado com média {:.1f}'.format(Media))
elif Media >5 and Media <=6.9:
    print('Aluno em recuperação com média {:.1f}'.format(Media))
elif Media >= 7:
    print('Aluno aprovado com média {:.1f}'.format(Media))
