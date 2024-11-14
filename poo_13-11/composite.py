from abc import ABC, abstractmethod

#component
class FileSystemComponent(ABC):

    def show_details(self):
        raise NotImplementedError

#leaf 
class File(FileSystemComponent):
    def __init__(self, nome: str)->None:
        self.nome = nome
      
    def show_details(self)->None:
        return print(f"File: {self.nome}")
    
#composite
class Directory(FileSystemComponent):
    def __init__(self, nome: str)->None:
        self.nome = nome
        self.components = []
    
    def add(self, component:FileSystemComponent)->None:
        self.components.append(component)

    def remove(self, component:FileSystemComponent)->None:
        self.components.remove(component)

    def show_details(self):
        print(f"Directory: {self.nome}")
        for component in self.components:
            component.show_details()

if __name__ == "__main__":

    file1 = File("arquivo.txt")
    file2 = File("arquivo.doc")
    file3 = File("arquivo.ppt")
    directory1 = Directory("Diretorio1")
    directory2 = Directory("Diretorio2")
    directory3 = Directory("Diretorio3")
    directory1.add(file1)
    directory2.add(file2)
    directory3.add(file3)
    directory1.remove(file1)
    root = Directory("Root")
    root.add(directory1)
    root.add(directory2)
    root.add(directory3)
    root.show_details()
    

    