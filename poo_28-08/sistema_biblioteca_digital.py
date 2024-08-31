from abc import ABC, abstractmethod

class Material_biblioteca(ABC):
    def __init__(self, titulo, autor, ano_publicação):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicação = ano_publicação

    @abstractmethod
    def get_informaçôes(self):
       pass

class Livro(Material_biblioteca):
    def __init__(self, titulo, autor, ano_publicação, volume, editora):
        super().__init__(titulo, autor, ano_publicação)
        self.volume = volume
        self.editora = editora
    def get_informaçôes(self):
         print(f"O titulo do livro é: {self.titulo}\n O nome do autor é: {self.autor}\n O ano de publicação é: {self.ano_publicação}")

class Revista(Material_biblioteca):
    def __init__(self, titulo, autor, ano_publicação, volume, editora):
        super().__init__(titulo, autor, ano_publicação)
        self.volume = volume
        self.editora = editora
    def get_informaçôes(self):
        print(f"O titulo do livro é: {self.titulo}\n O nome do autor é: {self.autor}\n O ano de publicação é: {self.ano_publicação}\n O volume é {self.volume}\n A editora é: {self.editora}")

class E_Bokk(Material_biblioteca):
    def __init__(self, titulo, autor, ano_publicação, volume, editora):
        super().__init__(titulo, autor, ano_publicação)
        self.volume = volume
        self.editora = editora
    def get_informaçôes(self):
        print(f"O titulo do livro é: {self.titulo}\n O nome do autor é: {self.autor}\n O ano de publicação é: {self.ano_publicação}\n O volume é {self.volume}\n A editora é: {self.editora}")

class Audiolivro(Material_biblioteca):
    def __init__(self, titulo, autor, ano_publicação, volume, editora):
        super().__init__(titulo, autor, ano_publicação)
        self.volume = volume
        self.editora = editora
    def get_informaçôes(self):
        print(f"O titulo do livro é: {self.titulo}\n O nome do autor é: {self.autor}\n O ano de publicação é: {self.ano_publicação}\n O volume é {self.volume}\n A editora é: {self.editora}")

class Biblioteca():
    def __init__(self):
        self.materiais = []

    def adicionar(self, material):
        self.materiais.append(material)

    def remover(self, material):
        self.materiais.remove(material)

    def info_material(self, material):
        material.get_informaçôes()

    def info_material_geral(self):
        for material in self.materiais:
            material.get_informaçôes()

biblioteca = Biblioteca()
livro = Livro("Harry Potter", "J.K. Rowling", 2000, 1, "abril")
livro2 = Livro("Harry Potter 2", "J.K. Rowling", 2004, 2, "abril")
livro3 = Livro("Harry Potter 3", "J.K. Rowling", 2009, 3, "abril")

revista = Revista("O bob", "Marley", 2023, "1 de muitos", "nenhuma")
revista2 = Revista("O bob a revolta", "Marley", 2028, "1 de muitos", "nenhuma")

biblioteca.adicionar(livro)
biblioteca.adicionar(livro2)
biblioteca.adicionar(livro3)
biblioteca.adicionar(revista)
biblioteca.adicionar(revista2)

biblioteca.remover(livro)

biblioteca.info_material_geral()