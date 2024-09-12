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
        super().__init__(nome, cargo)
        with open("poo_11-09/funcionarios.txt", "w", encoding="utf-8") as f:
            f.write(f"Nome: {nome}, Cargo: {cargo}")

    def listar_func(self):
        pass
   

    
