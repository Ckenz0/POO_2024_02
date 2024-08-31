from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, quantia, data):
        self.quantia = quantia
        self.data = data

    @abstractmethod
    def efetuar_pagamento(self):
        pass
        
class Dinheiro(Pagamento):
    def __init__(self, quantia, data, moeda):
        self.moeda = moeda
        super().__init__(quantia, data)

    def efetuar_pagamento(self):
        print(f"Pagamento no valor de {self.quantia} efetuado em {self.moeda}")
        
class Cartao(Pagamento):
    def __init__(self, quantia, data, numero_cartao, validade):
        self.numero_cartao = numero_cartao
        self.validade = validade
        super().__init__(quantia, data)

    def efetuar_pagamento(self):
        return (f'Pagamento efetuado com sucesso com o cartão no valor de {self.quantia}')
    
class Pix(Pagamento):
    def __init__(self, quantia, data, chave, banco):
        self.chave = chave
        self.banco = banco
        super().__init__(quantia, data)
    def efetuar_pagamento(self):
        print(f"Pagamento efetuado no banco na quantia de {self.quantia}\n Na data: {self.data}\n Pela chave: {self.chave}\n No banco: {self.banco}")

pag1 = Dinheiro(9000, "28/08/2024", "Reais")
pag2 = Cartao(1000, "18/08/2024", "US", 2018)
pag3 = Pix(5000, "22/08/2024", 111111, "inter")


pag1.efetuar_pagamento()
pag2.efetuar_pagamento()
pag3.efetuar_pagamento()