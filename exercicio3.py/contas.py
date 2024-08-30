"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta OK
    ContaCorrente deve ter um limite extra OK
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.



from abc import ABC, abstractmethod # Importando a abstração

class Conta(ABC): # Conta inicia com agencia conta saldo
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self._saldo = saldo # self._saldo = saldo Passa a valor como saldo

    @abstractmethod # Método abstrado conforme o exercício solicitou
    def sacar(self, valor):...

    @abstractmethod
    def depositar(self, valor):...

    def __repr__(self): # Representando meu objeto
        class_name = type(self).__name__  # Nome da classe
        attrs = f'{self.agencia!r} {self.conta!r} {self._saldo!r}' # Atributos!r
        return f'{class_name} {attrs}'

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self._saldo = saldo

    def sacar(self, valor): # Sacar recebe valor
        print('Conta Corrente R$', self._saldo) # Exibindo saldo
        novo_saldo = self._saldo - valor # VAR armazena saldo - valor a ser sacado
        self._saldo = novo_saldo # Atribuindo novo saldo
        if self._saldo < -300: # Atribuindo limite de R$ 300,00
            return 'Limite excedido'
        return f'Saque Conta corrente de R$ {valor}, Novo saldo R$ {self._saldo}.\n'

    def depositar(self, valor):
        print('Conta Corrente R$', self._saldo)
        depositado = self._saldo + valor
        self._saldo = depositado
        return f'Deposito Conta corrente de R$ {valor}, Novo saldo R$ {self._saldo}.\n'
    
class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self._saldo = saldo

    def sacar(self, valor):
        print('Conta Poupança R$', self._saldo)
        if self._saldo < valor: # Verificando saldo disponível
            return f'Saldo insuficiente! Saldo = {self._saldo}\nTentativa de saque {valor}\n' 
        sacado = self._saldo - valor
        self._saldo = sacado
        return f'Saque Conta poupança de R$ {valor}, Novo saldo R$ {self._saldo}.\n'

    def depositar(self, valor):
        print('Conta Poupança R$', self._saldo)
        depositado = self._saldo + valor
        self._saldo = depositado
        return f'Deposito Conta poupança de R$ {valor}, Novo saldo R$ {self._saldo}.\n'


def saque(conta: Conta, qnt): 
    executando = conta.sacar(qnt) # MESMA COISA QUE A LINHA 116 EM DIANTE
    print(executando)

def deposito(objeto: Conta, qnt):
    executando = objeto.depositar(qnt)
    print(executando)

if __name__ == '__main__':
    cp1 = ContaCorrente(3232, 2754, 3500)
    cc1 = ContaPoupanca(3232, 2345, 800)
    saque(cp1, 3400)
    deposito(cp1, 450)
    saque(cc1, 250)
    deposito(cc1, 600)
cp1 = ContaCorrente(123, 354, 4567) # Criando objeto para conta corrente
cc1 = ContaPoupanca(657, 5234, 345)
print(cp1.sacar(3400)) # Usando método sacar no meu objeto
print(cp1.depositar(450))
print(cc1.sacar(250))
print(cc1.depositar(600))
