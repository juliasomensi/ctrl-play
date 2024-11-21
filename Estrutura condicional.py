# idade =int(input("Digite sua idade: ")) 

# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# notas = int(input("Coloque sua nota aqui: "))

# if notas >= 7:
#    print("Você passou")
# elif notas <= 4:
#    print("Você está de rec")
# else: 
#    print("Exame")


idade = int(input("Digite sua idade"))
temCNH = True 

if idade >= 18 or temCNH:
    print("Pode dirigir")
else:
    print("Não vai poder dirigir")