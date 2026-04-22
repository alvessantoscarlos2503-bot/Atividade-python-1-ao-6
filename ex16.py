# exercício 16 - condição com AND

idade= int(input("Idade: "))
carteira = input("Tem carteira? (sim/não:  )")

if idade >= 18 and carteira == "sim":
    print("pode dirigir")
else:
    print("Não pode dirigir")