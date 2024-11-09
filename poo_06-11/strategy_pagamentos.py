from abc import ABC, abstractmethod

class FormaPagamentosStrategy(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCreditoStrategy(FormaPagamentosStrategy):
    def __init__(self, taxa_credito):
        self.taxa_credito = taxa_credito
    def processar_pagamento(self, valor_transacao):
        return valor_transacao * self.taxa_credito

class PaypalStrategy(FormaPagamentosStrategy):
    def __init__(self, taxa_paypal):
        self.taxa_paypal = taxa_paypal
    def processar_pagamento(self, valor_transacao):
        return valor_transacao * self.taxa_paypal

class TransferenciaBancariaStrategy(FormaPagamentosStrategy):
    def __init__(self, taxa_transferencia):
        self.taxa_transferencia = taxa_transferencia
    def processar_pagamento(self, valor_transacao):
        return valor_transacao * self.taxa_transferencia

class Pagamento:
    def __init__(self, estrategia: FormaPagamentosStrategy):
        self.estrategia = estrategia

    def processar_pagamento(self, valor):
        return self.estrategia.processar_pagamento(valor) + valor

if __name__ == "__main__":
    estrategia_cartao = CartaoCreditoStrategy(0.15)
    estrategia_paypal = PaypalStrategy(0)
    estrategia_transferencia = TransferenciaBancariaStrategy(0.05)

    valor_pag = 400
    
    pag1 = Pagamento(estrategia_cartao)
    print(f"O valor do pagamento por meio de cartão de credito é de: {pag1.processar_pagamento(valor_pag)}")

    pag2 = Pagamento(estrategia_paypal)
    print(f"O valor do pagamento por meio do Paypal é de: {pag2.processar_pagamento(valor_pag)}")

    pag3 = Pagamento(estrategia_transferencia)    
    print(f"O valor do pagamento por meio de transferência bancaria é de: {pag3.processar_pagamento(valor_pag)}")