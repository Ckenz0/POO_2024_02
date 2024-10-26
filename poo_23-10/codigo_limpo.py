from enum import Enum
from abc import ABC, abstractmethod

class Situacao(Enum):
    APROVADO = 1
    REPROVADO = 2
    RECUPERACAO = 3

def validar_valor(valor, minimo, maximo, nome_campo):
    if valor < minimo or valor > maximo:
        raise ValueError(f"Campo {nome_campo} deve estar entre os valores {minimo} e {maximo}")

def calcular_situacao_final(nota, frequencia):
    if nota >= 7 and frequencia >= 75:
        return Situacao.APROVADO
    elif nota >= 5 and frequencia >= 50:
        return Situacao.RECUPERACAO
    else:
        return Situacao.REPROVADO
    
class Registrar_Informacoes:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        validar_valor(nota, 0, 10, "Nota")
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)
    
    def definir_frequencia(self, frequencia):
        validar_valor(frequencia, 0, 100, "Frequência")
        self.frequencia = frequencia

class Estudante:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.registrar_info = Registrar_Informacoes()
        self.frequencia = 0.0
    
    def avaliar_situacao(self):
        media = self.registrar_info.calcular_media()
        return calcular_situacao_final(media, self.registrar_info.frequencia)
    
    def msgm_situacao(self):
        situacao = self.avaliar_situacao()
        if situacao == Situacao.APROVADO:
            return f"{self.nome} foi aprovado"
        elif situacao == Situacao.RECUPERACAO:
            return f"{self.nome} está de recuperação"
        else:
            return f"{self.nome} foi reprovado"

class Notificacao(ABC):
    @abstractmethod
    def enviar_notificacao(self, mensagem):
        pass

class Notificacao_sms(Notificacao):
    def enviar_notificacao(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class Notificacao_email(Notificacao):
    def enviar_notificacao(self, mensagem):
        print(f"Enviando email: {mensagem}")

class Servico_de_notificacoes:
    def __init__(self, notificadores):
        self.notificadores = notificadores

    def notificar(self, mensagem):
        for notificador in self.notificadores:
            notificador.enviar_notificacao(mensagem)

if __name__ == "__main__":
    estudante = Estudante("Carlos", 20, "12345")
    estudante.registrar_info.adicionar_nota(10)
    estudante.registrar_info.adicionar_nota(10)
    estudante.registrar_info.definir_frequencia(75)
    

    mensagem = estudante.msgm_situacao()
    print(mensagem)

    notificacao_email = Notificacao_email()
    notificacao_sms = Notificacao_sms()
    servico_de_notificacoes = Servico_de_notificacoes([notificacao_email, notificacao_sms])
    servico_de_notificacoes.notificar(mensagem)