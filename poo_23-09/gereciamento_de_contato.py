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
        raise NotImplementedError("Metodo implementado nas subclasses")

class ContatoPessoal(Contato):
    def __init__(self, nome, email, telefone, data_aniversario):
        super().__init__(nome, email, telefone)
        self.__data_aniversario = data_aniversario

    def get_data_aniversario(self):
        return self.__data_aniversario
        
    def set_data_aniversario(self, data_aniversario):
            self.__data_aniversario = data_aniversario
    
    def obter_informações(self):
        return print(f"Nome: {self.get_nome()}\n\
                     Email: {self.get_email()}\n\
                     Telefone: {self.get_telefone()}\n\
                     Data de aniversário: {self.__data_aniversario}")


class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def get_empresa(self):
        return self.__empresa
    
    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, cargo):
        self.__cargo = cargo
    
    def obter_informações(self):
        return print(f"Nome: {self.get_nome()} \n\
                    Email: {self.get_email()}\n\
                    Telefone: {self.get_telefone()}\n\
                    Empresa: {self.__empresa}\n\
                    Cargo: {self.__cargo}")

class GerenciadorContatos:
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect("poo_23-09/contatos.bd")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
        
    def criar_tabela(self):
        if self.conn:
            try:
                self.cursor.execute(''' CREATE TABLE IF NOT EXISTS contato
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    celular TEXT NOT NULL,
                                    aniversario TEXT,
                                    cargo TEXT,
                                    empresa TEXT,
                                    tipo TEXT NOT NULL)
                                    ''')
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela: {e}")
        else:
            print("Não é possivel criar tabela, não há conexão com o BD. ")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f"Erro ao fechar conexão. {e}")

    def inserir_contato_pessoal(self, contato):
        if self.conn:
            try:
                self.cursor.execute(''' INSERT INTO contato (nome, email, celular, aniversario, tipo)
                                    VALUES (?, ?, ?, ?, ?)
                                    ''', (contato.get_nome(), contato.get_email(), contato.get_telefone(), contato.get_data_aniversario(), "pessoal"))
                self.conn.commit()
                print(f"Contato pessoal {contato.get_nome()} adicionado")
            except sqlite3.Error as e:
                print(f"Erro ao inserir contato pessoal: {e}")

        else:
            print("Não foi possivel inserir contato, falha de conexão com o BD")

    def inserir_contato_profissional(self, contato):
        if self.conn:
            try:
                self.cursor.execute(''' INSERT INTO contato (nome, email, celular, cargo, empresa, tipo)
                                    VALUES (?, ?, ?, ?, ?, ?)
                                    ''', (contato.get_nome(), contato.get_email(), contato.get_telefone(), contato.get_cargo(), contato.get_empresa(), "profissional"))
                self.conn.commit()
                print(f"Contato profissional {contato.get_nome()} adicionado")
            except sqlite3.Error as e:
                print(f"Erro ao inserir contato profissional: {e}")
                
        else: 
            print("Não foi possivel inserir contato, falha de conexão com o BD")
            
    def atualizar_contato_pessoal(self, contato):
        if self.conn:
            try:
                self.cursor.execute(''' UPDATE contato SET email = ?, celular = ?, aniversario = ?
                                    WHERE nome = ? AND tipo = "pessoal"
                                    ''', (contato.get_email(), contato.get_telefone(), contato.get_data_aniversario(), contato.get_nome()))
                self.conn.commit()
                print(f"Contato pessoal {contato.get_nome()} atualizado")
            except sqlite3.Error as e:
                print(f"Erro ao atualizar contato pessoal: {e}")
        else:
            print("Não foi possível atualizar contato, falha de conexão com o BD")
    
    def atualizar_contato_profissional(self, contato):
        if self.conn:
            try:
                self.cursor.execute(''' UPDATE contato SET email = ?, celular = ?, cargo = ?, empresa = ?
                                    WHERE nome = ? AND tipo = "profissional"
                                    ''', (contato.get_email(), contato.get_telefone(), contato.get_cargo(), contato.get_empresa(), contato.get_nome()))
                self.conn.commit()
                print(f"Contato profissional {contato.get_nome()} atualizado")
            except sqlite3.Error as e:
                print(f"Erro ao atualizar contato profissional: {e}")
        else:
            print("Não foi possível atualizar contato, falha de conexão com o BD")

    def listar_contatos_pessoais(self):
        if self.conn:
            try:
                self.cursor.execute(''' SELECT * FROM contato WHERE tipo = "pessoal" ''')
                contatos = self.cursor.fetchall()
                for contato in contatos:
                    print(contato)
            except sqlite3.Error as e:
                print(f"Erro ao listar contatos pessoais: {e}")
        else:
            print("Não foi possível listar contatos, falha de conexão com o BD")

    def listar_contatos_profissionais(self):
        if self.conn:
            try:
                self.cursor.execute(''' SELECT * FROM contato WHERE tipo = "profissional" ''')
                contatos = self.cursor.fetchall()
                for contato in contatos:
                    print(contato)
            except sqlite3.Error as e:
                print(f"Erro ao listar contatos profissionais: {e}")
        else:
            print("Não foi possível listar contatos, falha de conexão com o BD")

    def listar_contatos(self):
        if self.conn:
            try:
                self.cursor.execute(''' SELECT * FROM contato ''')
                contatos = self.cursor.fetchall()
                for contato in contatos:
                    print(contato)
            except sqlite3.Error as e:
                print(f"Erro ao listar contatos: {e}")
        else:
            print("Não foi possível listar contatos, falha de conexão com o BD")

    def buscar_contato(self, nome):
        if self.conn:
            try:
                self.cursor.execute(''' SELECT * FROM contato WHERE nome = ? ''', (nome,))
                contato = self.cursor.fetchone()
                if contato:
                    print(contato)
                else:
                    print(f"Contato {nome} não encontrado")
            except sqlite3.Error as e:
                print(f"Erro ao buscar contato: {e}")
        else:
            print("Não foi possível buscar contato, falha de conexão com o BD")

if __name__ == "__main__":
    gerenciador = GerenciadorContatos()
    
    gerenciador.criar_tabela()

    contato_pessoal = ContatoPessoal('Jose', 'joao.silva@gmail.com', '1234-5678', '01/01/1990')
    gerenciador.inserir_contato_pessoal(contato_pessoal)
    
    contato_profissional = ContatoProfissional('Maria', 'maria.souza@gmail.com', '8765-4321', 'huawei', 'Gerente')
    gerenciador.inserir_contato_profissional(contato_profissional)
    
    gerenciador.listar_contatos()
    gerenciador.buscar_contato('Jose')
    gerenciador.fechar_conexao()