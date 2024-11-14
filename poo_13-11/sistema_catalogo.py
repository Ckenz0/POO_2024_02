"""
Você foi contratado para desenvolver um sistema de gerenciamento de catálogo para uma loja online. O sistema deve permitir que produtos individuais e categorias de produtos sejam gerenciados de maneira uniforme. A estrutura do catálogo deve permitir que cada categoria contenha produtos individuais e outras subcategorias.

Requisitos:

ü  Crie uma classe abstrata CatalogComponent com um método abstrato show_details.

ü  Crie uma classe Product que herda de CatalogComponent e implementa o método show_details para mostrar o nome e o preço do produto.

ü  Crie uma classe Category que herda de CatalogComponent.

ü  A classe category deve conter:

ü  Ter uma lista de componentes filhos (Product ou Category).

ü  Implementar métodos para adicionar e remover componentes.

ü  Implementar o método show_details para mostrar o nome da categoria e os detalhes de todos os componentes filhos.

ü  Implemente um código cliente que:

ü  Crie alguns produtos e categorias.

ü  Adicione produtos às categorias.

ü  Adicione categorias a outras categorias.

ü  Exiba a estrutura completa do catálogo chamando show_details na categoria raiz.
"""

from abc import ABC, abstractmethod

class CatalogComponent(ABC):
    @abstractmethod
    def show_details(self):
       raise NotImplementedError
    
class Product(CatalogComponent):
    def __init__(self, nome: str, preco: str)->None:
        self.nome = nome
        self.preco = preco
    
    def show_details(self):
        return print(f"Nome do produto: {self.nome}\nPreço do produto: {self.preco}")

class Category(CatalogComponent):
    def __init__(self, nome: str)->None:
        self.nome = nome
        self.products = []

    def add(self, product:CatalogComponent)->None:
        self.products.append(product)
    
    def remove(self, product:CatalogComponent)->None:
        self.products.remove(product)

    def show_details(self):
        print(f"Diretorio: {self.nome}")
        for product in self.products:
            product.show_details()

if __name__ == "__main__":
    produto1 = Product("Mascara", "R$:120,00")
    produto2 = Product("Garrafa", "R$:50,00")
    produto3 = Product("Conshifasai", "R$: 3000,00")
    categoria1 = Category("Diretorio1")
    categoria2 = Category("Diretorio2")
    categoria1.add(produto1)
    categoria2.add(produto2)
    categoria1.add(produto3)
    root = Category("Root")
    root.add(categoria1)
    root.add(categoria2)
    root.show_details()
    