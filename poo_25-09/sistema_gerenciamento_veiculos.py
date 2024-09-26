from abc import ABC, abstractmethod
from datetime import datetime

class Veiculo(ABC):
    quantidade_veiculos = 0
    def __init__(self, modelo, ano, valor):
        if Veiculo.validar_ano(ano):
            Veiculo.quantidade_veiculos += 1
            self.modelo = modelo
            self.ano = ano
            self.valor = valor
        else:
            print("O veiculo é muito velho")
            raise ValueError()
    @abstractmethod
    def calcular_seguro(self):
        raise NotImplementedError

    @staticmethod
    def validar_ano(ano):
        ano_atual = datetime.now().year
        return 2000 <= ano <=ano_atual+1
    
    @classmethod
    def total_veiculos(cls):
        return print(f"O total de veiculos armazenados é {cls.quantidade_veiculos}")

class Carro(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.10

class Moto(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.15

class Caminhao(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.20
    
def main():
    carro1 = Carro("Civic", 2025, 300000)
    carro2 = Carro("Uno", 2000, 400000)
    moto1 = Moto("Kawasaki", 2020, 150000)
    moto2 = Moto("Twister", 2018, 60000)
    caminhao1 = Caminhao("Scania Super", 2021, 250000)
    caminhao2 = Caminhao("Sprinter 417", 2020, 200000)

    carro1_seguro = carro1.calcular_seguro
    carro2_seguro = carro2.calcular_seguro
    moto1_seguro = moto1.calcular_seguro
    moto2_seguro = moto2.calcular_seguro
    caminhao1_seguro = caminhao1.calcular_seguro
    caminhao2_seguro = caminhao2.calcular_seguro

    print(f"{carro1} possui valor de seguro de {carro1_seguro}")
    print(f"{carro2} possui valor de seguro de {carro2_seguro}")
    print(f"{moto1} possui valor de seguro de {moto1_seguro}")
    print(f"{moto2} possui valor de seguro de {moto2_seguro}")
    print(f"{caminhao1} possui valor de seguro de {caminhao1_seguro}")
    print(f"{caminhao2} possui valor de seguro de {caminhao2_seguro}")

if __name__ == '__main__':
    main()