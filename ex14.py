# ex14 - faixa etária

idade = int(input("Digite a sua idade:  "))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("adulto")

else:
    print("Idoso")