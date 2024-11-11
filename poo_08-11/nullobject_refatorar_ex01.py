class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def cliente_info(self):
        print(f"Nome do cliente: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}")

class ClienteNull:
    def __init__(self):
        self.nome = "Desconhecido"

    def cliente_info(self):
        print("Cliente não encontrado.")
    
class Produto:
    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco
    
    def info_produto(self):
        print(f"Nome do produto: {self.nome_produto}\nPreço: {self.preco}")

class ProdutoNull:
    def info_produto(self):
        print("Produto não encontado.")

class Endereco:
    def __init__(self, rua, cidade, numero):
        self.rua = rua
        self.cidade = cidade
        self.numero = numero

    def info_endereco(self):
        print(f"Cidade: {self.cidade}\nEndereço: {self.rua}, {self.numero}")
    
class EnderecoNull:
    def info_endereco(self):
        print("Endereço não encontrado.")  

class PedidoFactory:

# Simulação de busca de dados
    def buscar_cliente(self, id):
        if id == 1:
            return Cliente("João", "joao@example.com", "4321452332")
        else:
            return ClienteNull()

    def buscar_produto(self, codigo):
        if codigo == "ABC":
            return Produto("Produto A", 100.0)
        else:
            return ProdutoNull()

    def buscar_endereco(self, cliente):
        if cliente and cliente.nome == "João":
            return Endereco("Rua Principal", "Cidade Exemplo", "337")
        else:
            return EnderecoNull()

# Código que contém múltiplas verificações de None
    def processar_pedido(self, cliente_id, codigo_produto):
        cliente = self.buscar_cliente(cliente_id)
        cliente.cliente_info()
        
        produto = self.buscar_produto(codigo_produto)
        produto.info_produto()
        
        endereco = self.buscar_endereco(cliente)
        endereco.info_endereco()

if __name__ == "__main__":
    factory = PedidoFactory()
    factory.processar_pedido(1, "ABC")
    factory.processar_pedido(2, "XYZ")