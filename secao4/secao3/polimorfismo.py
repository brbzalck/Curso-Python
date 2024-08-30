# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao): # Exemplo de polimorfismo - Independente da objeto instânciado, vai enviar notificação
    notificacao_enviada = notificacao.enviar() # Criando VAR que utiliza método abstrato da super class, com a notificação específica

    if notificacao_enviada: # NotificaçãoEmail
        print('Notificação enviada')
    else: #                   NotificaçãoSMS
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email) # Jogando meu objeto instânciado para dentro da função que polimorfa minha determinada notificação

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)