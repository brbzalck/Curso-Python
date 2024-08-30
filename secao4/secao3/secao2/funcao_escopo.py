"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Escopo local acessa escopo global, mas o global não consegue acessar o local
TUDO QUE ESTA DENTRO DA FUNÇÃO, ESTÁ PROTEGIDO NA FUNÇÃO
"""

x = 1 # x faz parte do escopo global, vai ser definido para toda extenxão do código


def escopo():
    # global x > má pratica de programação, mas pode fazer o valor de X dessa função ser o valor de X de todo código
    x = 10 # esse x faz parte dessa função escopo, e x vai ser igual a 10, apenas daqui para frente dentro no mundinho da função
 
    def outra_funcao(): # função dentro de outra função, onde um novo valor de X é definido para esse escopo da subfunção
        x = 11 # se não for definido o valor de X nessa função, x passa a ser 10 da sua função primária
        y = 2
        print(x, y) # exibindo o X com o valor definido no escopo dessa função == 11

    outra_funcao() # chamando função com o valor de x == 11
    print(x) # exibindo o valor de x == 10, pois nesse escopo x == 10(linha15)


print(x) # exibindo o valor de x == 1, pois x por enquanto nesse escopo global == 1
escopo() # chamando a função, o primeiro print da sub função retorna 11, e o segundo print da minha primeira função retorna 10
print(x) # exibindo x == 1 denovo, pois x desse escopo global não pode ser alterado pelo escopo fechado da função