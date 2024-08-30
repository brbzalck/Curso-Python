# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

import contas, pessoas # Importando para agregar

class Nubank:
    def __init__(self, agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None, # Especificando oque meus atributos vão receber
                 contas: list[contas.Conta] | None = None): # Ou lista específica Ou None
        self.agencias = agencias or []
        self.clientes = clientes or [] # Ou lista específica Ou lista vazia
        self.contas = contas or []

    # Se minha agencia recebida estiver nas agencias adicionadas na criação do objeto(linha74) - Check
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias: # agencia permanece apagado porque o python consegue buscar mesmo assim
            print('_checa_agencia', True) # agencia é um atriburo do objeto conta, criado no módulo contas
            return True
        print('_checa_agencia', False)
        return False
    
    # se meu cliente recebido estiver entre minha lista de clientes - Check
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
    
    # Se a conta recebida estiver entre minha lista de contas - check
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    # Se a conta recebida for atributo de cliente(linha70)
    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta: # Pegando o atributo agregado pela conta em cliente(linha70)
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
    
    # autenticar recebe como objeto o próprio Nubank()
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta): # Recebe cliente de Pessoa e conta de Conta
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)
    # Faz as verificações descritas nos métodos acima

    def __repr__(self): # Representando class_name, agencia clientes e contas
        class_name = type(self).__name__
        attrs = f'{self.agencias!r} {self.clientes!r} {self.contas!r}'
        return f'{class_name} {attrs}'


if __name__ == '__main__': 
    cliente1 = pessoas.Cliente('Lucas', 24) # Criando cliente com a classe Cliente
    contacorrente1 = contas.ContaCorrente(123, 123, 2500) # Jogando numa variável Classe que cria conta
    cliente1.conta = contacorrente1 # Criando conta para cliente
    cliente2 = pessoas.Cliente('Maria', 20)
    contacorrente2 = contas.ContaCorrente(234, 234, 2347)
    cliente2.conta = contacorrente2
    banco = Nubank() # Classe executa
    banco.clientes.extend([cliente1, cliente2]) # Adicionando na lista clientes Meus objetos instânciados de pessoas.Cliente
    banco.contas.extend([contacorrente1, contacorrente2]) # Adicionando na lista contas Meus objetos instânciados de contas.Conta
    banco.agencias.extend([2500, 123]) # Adicionando na lista agencias Meus objetos instânciados de contas.Conta

    if banco.autenticar(cliente1, contacorrente1): # Se Conseguir autenticar cliente1 e Contacorrente
        contacorrente1.depositar(10)
        cliente1.conta.depositar(100) # Deposita legal 100 pila :P
        print(cliente1.conta) # Lembrando: .conta trata-se de um conjunto de atributos módulo pessoas linha 70