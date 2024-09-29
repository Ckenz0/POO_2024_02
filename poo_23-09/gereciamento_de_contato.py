from abc import ABC, abstractmethod
import sqlite3

class Contato(ABC):
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        self.__telefone = telefone    

    @abstractmethod
    def obter_informações(self):
        pass

class ContatoPessoal(Contato):
    def __init__(self, nome, email, telefone, data_aniversaio):
        self.__data_aniversaio = data_aniversaio
        super.__init__(nome, email, telefone)

    def get_data_aniversario(self):
        return self.__data_aniversario
        
    def set_data_aniversario(self, data_aniversario):
            self.__data_aniversario = data_aniversario
    
    def obter_informações(self):
        return print(f"Nome: {self.nome} \
                     Email: {self.email}\
                     Telefone: {self.telefone}\
                     Data de aniversário: {self.__data_aniversaio}")


class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        self.__empresa = empresa
        self.__cargo = cargo
        super.__init__(nome, email, telefone)

        def get_empresa(self):
            return self.__empresa
        
        def set_empresa(self, empresa):
            self.__empresa = empresa

        def get_cargo(self):
            return self.__cargo
        
        def set_cargo(self, cargo):
            self.__cargo = cargo
        
         
        def obter_informações(self):
            return print(f"Nome: {self.nome} \
                        Email: {self.email}\
                        Telefone: {self.telefone}\
                        Empresa: {self.__empresa}\
                        Cargo: {self.__cargo}")

class GerenciadorContatos():
    def __init__(self):
        try:
            self.coon = sqlite3.connect("poo_23-09/gerenciamento_de_contato")
            self.cursor = self.coon.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
        
        def criar_tabela(self):
            if self.coon:
                try:
                    self.cursor.execute(''' CREATE TABLE IF NOT EXISTS contato
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome TEXT NOT NULL,
                                        email TEXT NOT NULL,
                                        celular TEXT NOT NULL,
                                        aniversario TEXT NOT NULL,
                                        cargo TEXT NOT NULL,
                                        empresa TEXT NOT NULL,
                                        tipo TEXT NOT NULL)
                                        ''')
                except sqlite3.Error as e:
                    print(f"Erro ao criar tabela: {e}")
            else:
                print("Não é possivel criar tabela, não há conexão com o BD. ")
        def fechar_conexao(self):
            if self.coon:
                try:
                    self.coon.close()
                except sqlite3.Error as e:
                    print(f"Erro ao fechar conexão. {e}")

    def Inserir_contato_pessoal():
        pass
    def Inserir_contato_profissional():
        pass
    def Atualizar_contato_pessoal():
        pass
    def Atualizar_contato_profissional():
        pass
    def Listar_contatos_pessoais():
        pass
    def listar_contatos_profissionais():
        pass
    def listar_contatos():
        pass
    def Buscar_contato():
        pass