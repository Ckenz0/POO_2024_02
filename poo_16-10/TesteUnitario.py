class Cadastro_Usuario:
    def __init__(self, nome, cpf, nascimento, endereco, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha

    def mostrar_info(Cadastro_Usuario):
        def __init__(self, nome, cpf, nascimento, endereco, telefone):
            super().__init__(nome, cpf, nascimento, endereco, telefone)
            print(f"Nome: {self.nome}\ CPF: {self.cpf}\ Data de nascimento: {self.nascimento}\ Endereço: {self.endereco}\ Telefone: {self.telefone}")

    def gravar_info(self):
        with open("poo_16-10/cadastro_<cpf>.txt", "w", encoding="utf-8") as f:
            f.write(f"Nome: {self.nome}\ CPF: {self.cpf}\ Data de nascimento: {self.nascimento}\ Endereço: {self.endereco}\ Telefone: {self.telefone}")

    def validar_nome(self):
        if len(self.nome.split()) > 2:
            True
        else:
            return False
    def validar_cpf():


            
  