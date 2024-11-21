# lado1 = float(input("Digite o primeiro lado: "))
# lado2 = float(input("Digite o segundo lado: "))
# lado3 = float(input("Digite o terceiro lado: "))

# if lado1 == lado2 == lado3:
#     print("Triângulo equilátero")
# elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#     print("Triângulo isósceles")
# else:
#     print("Escaleno")


# idade = int(input("Digite sua idade"))

# if idade <= 12:
#     print("Criança")
# elif idade <= 17:
#     print("Adolescente")
# elif idade <=60:
#     print("Adulto")
# elif idade <0 or idade > 120:
#     print("Inválida")
# else:
#     print("Idoso")

# peso = float(input("digite seu peso"))
# altura = float(input("coloque sua altura"))
# imc = peso / (altura ** 2)

# if imc < 18.5:
#    print("abaixo do peso")
# elif imc >= 18.6 or imc<= 24.9:
#      print("peso normal")
# elif imc >=25 or imc<= 29.9:
#     print("acima do peso")
# elif imc >=30 or imc<= 39.9:
#     print("obesidade grau 1")
# else:
#     print("obesidade grau 2")


nota1 = float(input("Digite sua nota"))
nota2 = float(input("Digite sua nota"))
nota3 = float(input("Digite sua nota"))
nota4 = float(input("Digite sua nota"))
media = (nota1 + nota2 + nota3 + nota4)/ 4

if media < 3:
    print("Reprovado")
elif media >=7:
    print("Aprovado")
else:
    print("Exame final")