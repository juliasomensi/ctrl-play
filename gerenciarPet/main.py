from gerenciarPet import gato, cachorro

def criarAnimal():
    nome = input("digite o nome do seu pet:")
    idade = int(input("digite a idade do seu pet:"))
    especie = input("é gato ou cachorro.").lower()

    if especie == "gato":
        return gato(nome, idade)
    elif especie == cachorro:
        return cachorro(nome, idade)
    else:
        print("tipo inválido. Criando um tipo padrão")
        return gato(nome, idade)

def menu():
    print("\nOque você quer fazer?")
    print("1- brincar")
    print("2-dormir")
    print("3- comer")
    print("4- ouvir o som")
    print("5- mostrar a energia")
    print("0- sair")

def main():
    pet = criarAnimal()
    while True:
        menu()
        escolha = input("escolha uma opção: ")

        if escolha == "1":
            horas = int(input("por quantas horas brincar? "))
            pet.brincar(horas)
        elif escolha == "2":
            horas = int(input("por quantas horas dormir? "))
            pet.dormir(horas)
        elif escolha == "3":
            comida = input("oque ele vai comer? ")
            pet.comer(comida)
        elif escolha == "4":
            pet.fazerSom()
        elif escolha == "5":
            print(f"Energia de {pet.nome}: {pet.energia}")
        elif escolha == "0":
            print("até mais")
            break
        else:
            print("opção inválida")

if __name__ == "__main__":
    main()