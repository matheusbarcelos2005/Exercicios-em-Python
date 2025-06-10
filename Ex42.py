r1 = float(input('Digite o primeiro segmento:  '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 and r2 == r3:
        print('Formam um triângulo equilátero.')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Formam um triângulo escaleno.')
    else:
        print('Formam um triângulo isósceles.')
else:
    print('Os segmentos não podem formar um triângulo.')