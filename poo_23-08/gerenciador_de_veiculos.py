'''Proposto: Sistema de Gestão de Veículos
Objetivo do Exercício: Praticar os conceitos de orientação a objetos, herança, e
polimorfismo em Python. O exercício envolve a criação de um sistema de gestão de
veículos em uma concessionária, distinguindo diferentes tipos de veículos e
implementando funcionalidades específicas para cada um.
Descrição do Sistema: O sistema deverá permitir o cadastro de veículos, distinguindo
entre carros, motos e caminhões. Cada tipo de veículo terá atributos e métodos
específicos. O sistema será composto pelas seguintes classes, métodos e atributos:
Classes, Métodos e Atributos
Classe Veiculo (Classe Base)
- Atributos:
 - `marca`
 - `modelo`
 - `preco_base`
- Métodos:
 - `__init__()` para inicializar os atributos comuns.
 - `calcular_valor_venda()` (método abstrato a ser implementado nas subclasses).
Classe Carro (herda de Veiculo)
- Atributos adicionais:
 - `num_portas`
 - `ar_condicionado` (booleano)
- Métodos:
 - `__init__()` para inicializar os atributos do carro.
 - `calcular_valor_venda()` (considerando o valor base e um acréscimo se houver arcondicionado).
Classe Moto (herda de Veiculo)
- Atributos adicionais:
 - `cilindradas`
- Métodos:
 - `__init__()` para inicializar os atributos da moto.
 - `calcular_valor_venda()` (considerando o valor base e o número de cilindradas).
Classe Caminhao (herda de Veiculo)
- Atributos adicionais:
 - `capacidade_carga`
 - `eixos`
- Métodos:
 - `__init__()` para inicializar os atributos do caminhão.
 - `calcular_valor_venda()` (considerando o valor base, a capacidade de carga e o
número de eixos).
Classe Concessionaria
- Atributos:
 - `veiculos` (lista de objetos `Veiculo`).
- Métodos:
 - `adicionar_veiculo()` para incluir um novo veículo na lista.
 - `calcular_valor_estoque()` para calcular o valor total do estoque de veículos.
 - `exibir_menu()` para exibir o menu de opções e permitir a interação com o usuário.
Funcionalidades do Menu:
- Incluir Veículo: Solicita informações sobre o veículo e o adiciona ao sistema.
- Calcular Valor do Estoque: Calcula e exibe o valor total do estoque de veículos na
concessionária.
- Sair: Encerra o programa.
Estrutura de Dados:
- Os veículos devem ser armazenados em uma lista, sendo identificados pela
combinação de marca e modelo, ou por um atributo único que o usuário pode definir.
Justificativa para o Uso de Herança:
1. Hierarquia Clara:
 Carros, Motos, e Caminhões herdam características comuns de `Veiculo`, facilitando o
reaproveitamento de código e a estruturação do sistema.

2. Polimorfismo:
 Cada tipo de veículo implementa sua própria versão do método
`calcular_valor_venda()`, o que permite a flexibilidade de calcular o valor de venda de
forma específica para cada tipo de veículo.

3. Extensibilidade:
 Novos tipos de veículos podem ser facilmente adicionados ao sistema no futuro sem
alterar as classes existentes, o que facilita a manutenção e evolução do código.'''

class Veiculo:
    def __init__(self, marca, modelo, preco_base):
        self.marca = marca
        self.modelo = modelo
        self.preco_base = preco_base
    def calcular_valor_venda(self):
        raise NotImplementedError("Esse método deve ser implementado nas subclasses")

class Carro(Veiculo):
    def __init__(self, marca, modelo, preco_base, num_portas, ac):
        super(). __init__(self, marca, modelo, preco_base)
        self.num_portas = num_portas
        self.ac = ac
    def calcular_valor_venda(self):
        if self.ac:
            valor_ac = 5000
        else:
            valor_ac = 0
        return self.preco_base + valor_ac

class Moto(Veiculo):
    def __init__(self, marca, modelo, preco_base, cilindradas):
        super(). __init__(self, marca, modelo, preco_base)
        self.cilindradas = cilindradas
    def calcular_valor_venda(self):
        return self.preco_base + self.cilindradas * 10

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, preco_base, cap_cargas, eixos):
        super(). __init__(self, marca, modelo, preco_base)
        self.cap_cargas = cap_cargas
        self.eixos = eixos
    def calcular_valor_venda(self):
        return self.preco_base + self.cap_cargas * 10 + self.eixos * 500

class Concessionaria:
    def __init__(self):
        self.veiculos = []
    def adicionar_veiculo(self, add_veiculo):
        self.veiculos.append(add_veiculo)
    def calcular_valor_estoque(self):
        pass
    def exibir_menu(self):
        print("Menu de opções: \n")
        print("1 - Adicionar veículo ao estoque")
        print("2 - Calcular valor do estoque")
        print("3 - Sair")
        escolha = int(input("Escolha umas das opções: "))
        if escolha == 1:
            self.marca = input("Digite a marca do veículo: ")
            self.semodelo = input("Digite o modelo do veículo: ")
            self.preco_base = float(input("Digite o preço base do veículo: "))
            
    def incluir_veiculo_menu():
        pass