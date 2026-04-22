# ex19 - Prioridade
idade = int(input("Idade:  "))
gestante = input("é gestante (sim ou não): ")

if idade >= 60 or gestante == "sim":
    print("senha preferencial")

else:
    print("Atendimento normal")