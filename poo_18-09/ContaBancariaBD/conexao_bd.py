import sqlite3

class ConexaoBD:
    def __init__(self):
        try:
            self.coon = sqlite3.connect('banco.bd')
            self.cursor = self.coon.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela(self):
        if self.coon:
            try:
                self.cursor.execute(''' CREATE TABLE IF NOT EXISTS contas
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    numero_conta INTEGER NOT NULL,
                                    titular TEXT NOT NULL)
                                    ''')
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela: {e}")
        else:
            print("Não é possivel criar a tabela, não há conexão com o BD.")
    def fechar_conexao(self):
        if self.coon:
            try:
                self.coon.close()
            except sqlite3.Error as e:
                print(f"Erro ao fechar conexão. {e}")

#exemplo de uso
##conexao = ConexaoBD()
#conexao.criar_tabela()
#conexao.fechar_conexao()