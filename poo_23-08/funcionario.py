class Funcionario:
    def __init__(self,nome,id,salario):
        self.nome = nome
        self.id = id
        self.salario = salario
    def mostrar_detalhes(self):
        print(f"nome: {self.nome}\n id: {self.id} salario:\n {self.salario}")
    def calcular_bonificacao(self):
        return self.salario*12*0.6

class Gerente(Funcionario):
    def __init__(self,nome,id,salario):
        super().__init__(self,nome,id,salario)
    def calcular_bonificacao(self):
        return self.salario*12*0.8
    
class Engenheiro(Funcionario):
    def __init__(self,nome,id,salario,especificacao):
        self.especificacao = especificacao
        super().__init__(self,nome,id,salario)
    def calcular_bonificacao(self):
        return self.salario*12*0.8
    def mostrar_detalhes(self):
        print(f"nome: {self.nome}\n id: {self.id}\n salario: {self.salario}\n especialidade: {self.especificacao}")

func1 = Funcionario("Cleber", 1, 1500)
func2 = Funcionario("Bruno", 2, 1500)
gerente1 = Gerente("Alex", 3, 5500)
gerente2 = Gerente("Nilton", 4, 4500)
eng1 = Engenheiro("Bia", 5, 7500, "Eng.computacao")
eng2 = Engenheiro("Matheus", 6, 7500, "Eng.producao")

bonus_func1 = func1.calcular_bonificacao()
bonus_func2 = func2.calcular_bonificacao()
bonus_gerente1 = gerente1.calcular_bonificacao()
bonus_gerente2 = gerente2.calcular_bonificacao()
bonus_eng1 = eng1.calcular_bonificacao()
bonus_eng2 = eng2.calcular_bonificacao()
print(bonus_eng1)