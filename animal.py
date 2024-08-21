#Declaração da classe
class Animal:
    
    #Metodo construtor da classe executado sempre que um objeto é criado
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som
    def setSom(self, som):
        self.som = som

    def fazerSom(self):
        print(f"O {self.nome} faz {self.som}")

    def alimentar(self):
        print(f"O {self.nome} está comendo")

    def dormir(self):
        print(f"O {self.nome} está dormindo")

    def mostrarInfo(self):
        print(f"O nome do animal é {self.nome}")
        print(f"O tipo do animal é {self.tipo}")
        print(f"O som do animal é {self.som}")

animal1 = Animal("do", "cachorro", "mia")
animal2 = Animal("Ab", "gato", "late")
animal1.setSom("auau")
animal1.fazerSom()
animal1.alimentar()
animal1.dormir()
animal1.mostrarInfo()