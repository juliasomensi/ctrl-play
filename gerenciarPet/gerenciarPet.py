class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100
    
    def fazerSom(self):
        print(f"{self.nome} fez um som")

    def dormir(self, horas):
        energiaGanha = horas * 10
        self.energia = self.energia + energiaGanha
        if self.energia >=100:
            self.energia = 100
        print(f"{self.nome} dormiu por {horas} e ganhou {energiaGanha} de energia. Energia atual: {self.energia}")

    def brincar(self, horas):
        energiaGasta = horas * 8
        self.energia = self.energia - energiaGasta
        if self.energia <=0:
            self.energia = 0
            print(f"{self.nome} está muito cansado para brincar")
        else:
            print(f"{self.nome} brincou por {horas} e perdeu {energiaGasta} de energia. Energia atual {self.energia}")

    def comer(self, comida):
        energiaGanha = 35 
        self. energia += energiaGanha
        if self.energia >=100:
            self.energia = 100
            print(f"{self.nome} está muito cheio e não consegue mais comer")
        else:
            print(f"{self.nome} comeu {comida} e ganhou {energiaGanha} de energia. Energia atual: {self.energia}") 

class gato(animal):
    def fazerSom(self):
        print(f"{self.nome} diz: miau")

class cachorro(animal):   
    def fazerSom(self):
        print(f"{self.nome} diz: auau")    
