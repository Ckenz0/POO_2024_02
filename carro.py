class Carro:

    def __init__(self,modelo,marca,ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.desligar = False

    def infoCarro(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano} \nLigado: {self.ligado}")

carro1 = Carro("Chronos", "Fiat", "2025")
carro1.ligar()
carro1.infoCarro()
