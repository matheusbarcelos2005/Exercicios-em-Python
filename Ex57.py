sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite o sexo (M/F): ')).strip().upper()[0]
print(f'Sexo {} registrado com sucesso!'.format(sexo))