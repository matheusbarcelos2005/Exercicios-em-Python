
pesomaior = 0
pesomenor = 0
for pessoas in range (1,5+1):
    Peso = float(input('Quanto a pessoa {}º pesa? '.format(pessoas)))
    if Peso == 1:
        pesomaior = pessoas
        pesomenor = pessoas
    else:
        if Peso > pesomaior:
            pesomaior = Peso
        if Peso < pesomenor:
            pesomenor = Peso
print('A pessoa mais pesada, pesa {} quilos'.format(pesomaior))
print('A pessoa mais leve, pesa {} quilos'.format(pesomenor))
