"""Sistema de Gerenciamento de Viagens
Objetivo: Desenvolver um sistema para gerenciar viagens utilizando herança,
polimorfismo, classes abstratas e métodos abstratos.
Descrição:
Você está desenvolvendo um sistema para uma agência de viagens que oferece
diferentes tipos de viagens, como pacotes de cruzeiros, pacotes terrestres, e pacotes
aéreos. Cada tipo de viagem possui características distintas, mas há atributos e
métodos que são comuns a todas as viagens.
Requisitos:
1. Crie uma classe abstrata Viagem, que terá os atributos comuns como destino,
duracao, e precoBase, e um método abstrato calcular_preco_total() para calcular
o custo total da viagem.
2. Crie subclasses Cruzeiro, ViagemTerrestre, e ViagemAerea, cada uma
implementando o método calcular_preco_total() de acordo com suas regras
específicas (por exemplo, taxas de serviço para cruzeiros ou passagens adicionais
para viagens aéreas).
3. Utilize polimorfismo para calcular o preço total das viagens de maneira dinâmica,
dependendo do tipo de viagem.
4. Crie uma classe AgenciaViagens, que será responsável por gerenciar as viagens e
calcular o custo total das viagens vendidas.
Exemplo de funcionalidades:
• adicionar_viagem(): adiciona uma nova viagem ao sistema.
• calcular_receita_total(): calcula o valor total de todas as viagens vendidas.
• exibir_detalhes_viagem(): exibe os detalhes completos de uma viagem
específica."""

from abc import ABC, abstractmethod

class Viagem(ABC):
    def __init__(self, destino, duracao, precoBase):
        self.destino = destino
        self.duracao = duracao
        self.precoBase = precoBase

    @abstractmethod
    def calcular_preco_total(self):
        pass

class Cruzeiro(Viagem):
    def __init__(self, destino, duracao, pracoBase, taxaServico, taxaSeguro):
        super().__init__(destino, duracao, pracoBase)
        self.taxaServico = taxaServico
        self.taxaSeguro = taxaSeguro

    def calcular_preco_total(self):
        if self.taxaSeguro:
            valor_taxaSeguro = 300
        else:
            self.valor_taxaSeguro = 0
        
        if self.taxaServico:
            valor_taxaServico = 500
        else:
            valor_taxaServico = 0
        
        return self.precoBase + valor_taxaSeguro + valor_taxaServico

class ViagemTerrestre(Viagem):
    def __init__(self, destino, duracao, precoBase, taxaSeguro, guia):
        super().__init__(destino, duracao, precoBase)
        self.taxaSeguro = taxaSeguro
        self.guia = guia

    def calcular_preco_total(self):
        if self.taxaSeguro:
            valor_taxaSeguro = 300
        else:
            self.valor_taxaSeguro = 0
        
        if self.guia:
            valor_guia = 100
        else:
            valor_guia = 0
        
        return self.precoBase + valor_taxaSeguro + valor_guia

class ViagemAerea(Viagem):
    def __init__(self, destino, duracao, precoBase, taxaSeguro, classe):
        super().__init__(destino, duracao, precoBase)
        self.taxaSeguro = taxaSeguro
        self.classe = classe

    def calcular_preco_total(self):
        if self.taxaSeguro:
            valor_taxaSeguro = 1500
        else:
            self.valor_taxaSeguro = 0
        
        if self.classe:
            valor_classe = 2000
        else:
            valor_classe = 0
        
        return self.precoBase + valor_taxaSeguro + valor_classe
    
class AgenciaViagens(Viagem):
    pass