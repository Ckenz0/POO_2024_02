class Pessoa():
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
 
class Paciente():
    def __init__(self, pessoa: Pessoa):
        self.pessoa = pessoa

class Medico():
    def __init__(self, pessoa: Pessoa, crm, especialidade):
        self.pessoa = pessoa
        self.crm = crm
        self.especialidade = especialidade

class Consulta():
    def __init__(self, paciente: Paciente, medico: Medico, data_hora, observacoes):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.observacoes = observacoes

class Menu():
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.consultas = []

    def incluir_medico(self):
        nome = input("Insira o seu nome: ")
        cpf = input("Insira o seu cpf: ")
        data_nascimento = input("Insira a sua data de nascimento: ")
        crm = input("Insira o seu crm: ")
        especialidade = input("Insira a sua especialidade: ")
        pessoa = Pessoa(nome, cpf, data_nascimento)
        medico = Medico(pessoa, crm, especialidade)
        self.medicos[crm] = medico
        print("Medico adicionado com sucesso!!!")

    def incluir_paciente(self):
        nome = input("Insira o seu nome: ")
        cpf = input("Insira o seu cpf: ")
        data_nascimento = input("Insira a sua data de nascimento: ")
        pessoa = Pessoa(nome, cpf, data_nascimento)
        paciente = Paciente(pessoa)
        self.pacientes[cpf] = paciente
        print("Paciente adicionado com sucesso!!!")

    def agendar_consulta(self):
        cpf_paciente = input("CPF do paciente: ")
        crm_medico = input("CRM do medico: ")
        data_hora = input("Data e hora da consulta: ")
        observacoes = input("Observações: ")
        if cpf_paciente in self.pacientes:
           paciente = self.pacientes[cpf_paciente]

        else: 
            return "Paciente não cadastrado!!"

        if crm_medico in self.medicos:
            medico = self.medicos[crm_medico]

        else:
            return "Medico não cadastrado!!"
        
        if paciente and medico:
            consulta = Consulta(paciente, medico, data_hora, observacoes)
            self.consultas.append(consulta)
            print("Consulta agendada!")
        

    def ver_agenda(self):
        if not self.consultas:
            return "Nenhuma consulta cadastrada"
        for consulta in self.consultas:
            print(f"Consulta: {consulta.data_hora}, Paciente: {consulta.paciente.pessoa.nome}, Médico:{consulta.medico.pessoa.nome}")
            
    def exibir_menu(self):
        while True:
            print("Bem vindo ao menu da clinica, escolha uma das opções abaixo: \n\
                1) Incluir medico\n\
                2) Incluir paciente\n\
                3) Agendar consulta\n\
                4) Ver agenda\n\
                5) Sair\n")
            opcao = int(input("Digite o número da opção:  "))
            if opcao == 1:
                self.incluir_medico()
            elif opcao == 2:
                self.incluir_paciente()
            elif opcao == 3:
                self.agendar_consulta()
            elif opcao == 4:
                self.ver_agenda()
            elif opcao == 5:
                print("Obrigado por usar o programa")
                break
            else:
                print("Opção invalida!!!")


if __name__=="__main__":
    menu = Menu()
    menu.exibir_menu()