import re
from datetime import datetime

class CadastroUsuario:
    def __init__(self, nome, cpf, nascimento, endereco, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha

    def validar_nome(self):
        if self.nome and len(self.nome.split()) >= 2:
            return True
        raise ValueError("Nome inválido: o nome deve conter pelo menos duas palavras.")

    def validar_cpf(self):
        padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(padrao_cpf, self.cpf):
            return True
        raise ValueError("CPF inválido: o formato deve ser XXX.XXX.XXX-XX.")

    def validar_nascimento(self):
        try:
            data_nascimento = datetime.strptime(self.nascimento, "%d/%m/%Y")
            if data_nascimento < datetime.now():
                return True
            else:
                raise ValueError("Data de nascimento inválida: a data não pode estar no futuro.")
        except ValueError:
            raise ValueError("Data de nascimento inválida: o formato deve ser DD/MM/AAAA.")

    def validar_endereco(self):
        if self.endereco.strip():
            return True
        raise ValueError("Endereço inválido: o endereço não pode ser vazio.")

    def validar_telefone(self):
        padrao_telefone = r'^\(\d{2}\) \d{4,5}-\d{4}$'
        if re.match(padrao_telefone, self.telefone):
            return True
        raise ValueError("Telefone inválido: formatos aceitos são (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.")

    def validar_senha(self):
        if len(self.senha) >= 8 and any(char.isdigit() for char in self.senha) and any(char.isalpha() for char in self.senha):
            return True
        raise ValueError("Senha inválida: a senha deve ter pelo menos 8 caracteres, incluindo letras e números.")

    def mostrar_info(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")

    def gravar_info(self):
        # Validação de todos os dados antes de gravar no arquivo
        if all([
            self.validar_nome(),
            self.validar_cpf(),
            self.validar_nascimento(),
            self.validar_endereco(),
            self.validar_telefone(),
            self.validar_senha()
        ]):
            nome_arquivo = f"cadastro_{self.cpf}.txt"
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(f"Nome: {self.nome}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")
            print(f"Dados gravados com sucesso em {nome_arquivo}.")