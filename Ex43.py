peso = float(input('Digite seu peso atual(Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif imc >= 18.5 and imc < 25:
     print('Você está no seu peso ideal {:.1f}.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')