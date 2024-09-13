class GerenciarArquivos:
    def __init__(self, nome, cargo, arquivo):
        self.nome = nome
        self.cargo = cargo
        self.arquivo = arquivo
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                f.read(f)
        except Exception as e:
            self.funcionarios = {}
    
    def inserir_func(self, nome, cargo):
        with open("poo_11-09/funcionarios.txt", "w", encoding="utf-8") as f:
            f.write(f"Nome: {nome}, Cargo: {cargo}")

    def listar_func(self):
        with open("poo_11-09/funcionarios.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
            print(conteudo)

    def imprimir_info(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}")
    

gerenciador = GerenciarArquivos("Caue", "Developer", "poo_11-09/funcionarios.txt")
gerenciador.inserir_func("João", "Analista")
gerenciador.inserir_func("Maria", "Gerente")
gerenciador.listar_func()
gerenciador.imprimir_info()
    
