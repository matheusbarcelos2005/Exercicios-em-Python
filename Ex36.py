casa = float(input("Digite o valor da casa: R$ "))
salarioComprador = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Digite em quantos anos será pago: "))
prestacao  = casa  / (anos * 12)
print("Para pagar uma casa em {} anos a prestação será de R$ {:.2f}".format(anos, prestacao))
if prestacao > (salarioComprador * 0.3):
    print("Empréstimo negado!, pois a prestação ultrapassa 30% do salário.")
else:
    print("Empréstimo aprovado!, pois a prestação não ultrapassa 30% do salário.")
