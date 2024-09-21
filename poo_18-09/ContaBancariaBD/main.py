from conexao_bd import ConexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__=="__main__":
    conexao = ConexaoBD()
    conexao.criar_tabela()

    conta1 = ContaBancaria(999909, "Cauê Kenzo Adaniya", 100000, 200000)
    conta2 = ContaBancaria(999919, "Bruno Marques", 99999999, 100000)

    conta1.sacar(40000)
    conta1.depositar(1)
    conta1.exibir_info()
    conta2.exibir_info()
    conta_dao = ContaBancariaDAO(conexao)
    conta_dao.salvar_conta(conta1)
    conta_dao.salvar_conta(conta2)
    conexao.fechar_conexao()
    