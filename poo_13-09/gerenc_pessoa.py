import pickle as pkl

class Cliente:
    def __init__(self, nome, email, ids):
        self.ids = ids
        self.nome = nome
        self.email = email

class PessoaFisica(Cliente):
    def __init__(self, nome, email, cpf, ids):
        super(). __init__(nome, email, ids)
        self.cpf = cpf
class PessoaJuridica(Cliente):
    def __init__(self, nome, email, cnpj, ids):
        super(). __init__(nome, email, ids)
        self.cnpj = cnpj
        
class GerenciadorDeClientes:
    def __init__(self):
        self.cliente_pf = []
        self.cliente_pj = []
        self.ids_contador = 1

    def adicionar_cliente_pf(self):
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        cpf = str(input("CPF: "))
        cliente = PessoaFisica(nome, email, cpf, self.ids_contador)
        self.cliente_pf.append(cliente)
        self.ids_contador += 1

    def adicionar_cliente_pj(self):
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        cnpj = str(input("CNPJ: "))
        cliente = PessoaJuridica(nome, email, cnpj, self.ids_contador)
        self.cliente_pj.append(cliente)
        self.ids_contador += 1
    
    def listar_clientes(self):
        for pf in self.cliente_pf:
            print(f"ID: {pf.ids}; Nome: {pf.nome}; Email: {pf.email}; CPF = {pf.cpf}")
        for pj in self.cliente_pj:
            print(f"ID: {pj.ids} Nome: {pj.nome}; Email: {pj.email}; CNPJ = {pj.cnpj}")

    def buscar_cliente_pf(self):
            ids = int(input("Digite o ID do cliente: "))
            for cliente in self.cliente_pf:
                if cliente.ids == ids:
                    print(f"ID: {cliente.ids}; Nome: {cliente.nome}; Email: {cliente.email}; CPF: {cliente.cpf}")
                    return cliente
            print("Cliente não encontrado")
            return None    

    def buscar_cliente_pj(self):
            ids = int(input("Digite o ID do cliente: "))
            for cliente in self.cliente_pj:
                if cliente.ids == ids:
                    print(f"ID: {cliente.ids}; Nome: {cliente.nome}; Email: {cliente.email}; CNPJ: {cliente.cnpj}")
                    return cliente
            print("Cliente não encontrado")
            return None

    def excluir_cliente_pf(self):
            ids = int(input("Digite o ID do cliente: "))
            for cliente in self.cliente_pf:
                if cliente.ids == ids:
                    self.cliente_pf.remove(cliente)
                    print("Cliente excluído com sucesso!")
                    return
            print("Cliente não encontrado")

    def excluir_cliente_pj(self, ids):
        ids = int(input("Digite o ID do cliente: "))
        for cliente in self.cliente_pj:
            if cliente.ids == ids:
                self.cliente_pj.remove(cliente)
                print("Cliente excluído com sucesso!")
                return
        print("Cliente não encontrado")

    def salvar_dados(self):
        with open("poo_13-09/Lista_pessoa_pf.pkl", "wb") as f:
            pkl.dump(self.cliente_pf, f)
    
        with open("poo_13-09/Lista_pessoa_pj.pkl", "wb") as f:
            pkl.dump(self.cliente_pj, f)

    def carregar_dados(self):
        try:
            with open("poo_13-09/Lista_pessoa_pf.pkl", "rb") as f:
                self.cliente_pf = pkl.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            self.cliente_pf = []
        try:
            with open("poo_13-09/Lista_pessoa_pj.pkl", "rb") as f:
                self.cliente_pj = pkl.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            self.cliente_pj = []

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
                self.excluir_cliente_pf()
            elif escolha == 7:
                self.excluir_cliente_pj()
            elif escolha == 8:
                self.salvar_dados()
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")           

if __name__ == "__main__":
    gerenciador = GerenciadorDeClientes()
    gerenciador.carregar_dados()
    gerenciador.menu_interativo()