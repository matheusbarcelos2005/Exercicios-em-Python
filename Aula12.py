nome = str(input("Digite seu nome: "))
if nome == 'Gustavo':
    print("Que nome bonito!")
    print("Bom dia, {}!".format(nome))
elif nome == 'Pedro'or nome == 'Maria':
    print("Seu nome é bem popular!")
    print("Bom dia, {}!".format(nome))
else:
    print("Bom dia, {}!".format(nome))