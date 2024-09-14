import pickle as pkl

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class PessoaFisica:
    def __init__(self, nome, email, cpf):
        self.cpf = cpf
        super(). __init__(nome, email)

class PessoaJuridica:
    def __init__(self, nome, email, cnpj):
        self.cnpj = cnpj
        super(). __init__(nome, email)

class GerenciadorDeClientes:
    def adicionar_cliente_pf(self):
        self.cliente_pf = []
        with open("Lista_pessoa_pf.pkl", "wb") as pf:
            pkl.dump(self.cliente_pf, pf)


    def adicionar_cliente_pj(self):
        self.cliente_pj = []
        with open("Lista_pessoa_pj.pkl", "wb") as pj:
            pkl.dump(self.cliente_pj, pj)


    def listar_clientes(self):
        for i in range(len(self.cliente_pf)):
            print(f"Nome: {self.nome}; Email: {self.email}; CPF = {self.cpf};
                CNPJ = {self.cnpj}")
        for i in range(len(self.cliente_pj)):
            print(f"Nome: {self.nome}; Email: {self.email}; CPF = {self.cpf};
                CNPJ = {self.cnpj}")

    def buscar_cliente_pf(self):
        if self.nome in self.cliente_pf:
            return self.cliente_pf[self.nome]

    def buscar_cliente_pj(self):
        if self.nome in self.cliente_pj:
            return self.cliente_pj[self.nome]

    def excluir_cliente_pf(self):
        pass

    def excluir_cliente_pj(self):
        pass

    def salvar_dados(self):
        pass

    def menu_interativo(self):
        while True:
            print("Bem vindo ao menu de gerenciamente de clientes!!! \n"
                "Escolha uma das seguintes opções: ")
            print("\n1 - Adicionar Cliente (Pessoa Física)")
            print("2 - Adicionar Cliente (Pessoa Jurídica)")
            print("3 - Listar Clientes")
            print("4 - Buscar Cliente (Pessoa Física por ID)")
            print("5 - Buscar Cliente (Pessoa Jurídica por ID)")
            print("6 - Excluir Cliente (Pessoa Física por ID)")
            print("7 - Excluir Cliente (Pessoa Jurídica por ID)")
            print("8 - Salvar Dados e Sair")
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                self.adicionar_cliente_pf()
            elif escolha == 2:
                self.adicionar_cliente_pj()
            elif escolha == 3:
                self.listar_clientes()
            elif escolha == 4:
                self.buscar_cliente_pf()
            elif escolha == 5:
                self.buscar_cliente_pj()
            elif escolha == 6:
                self.excluir_cliente_pf
            elif escolha == 7:
                self.excluir_cliente_pj()
            elif escolha == 8:
                self.salvar_dados()
            else:
                print("Opção inválida. Por favor, tente novamente.")           

if __name___ == __main__: