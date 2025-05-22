"""
Básica
^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$
https://regex101.com/r/9s4bgv/1/

Básica 2
^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$
https://regex101.com/r/mH4ChC/2/

rfc 5322
^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
https://regex101.com/r/fkxI15/1/
"""

import re

emails = """
Valid email addresses
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com

Invalid email addresses
Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""


email_validator = re.compile(
    # ^$ padrão para buscar no começo ao fim da linha

    # \w+ para pegar de A-Za-z0-9_, + o tanto que tiver de A-Za-z0-9_

    # ?: diz que a condicional não precisa dar retorno separado, apenas de confirmação
    # adicionando ao grupo de a-z os caracteres permitidos no email . \-(traço espacado) +!%
    # após os caracteres especiais, exige UM ou mais Caracteres

    # * esse grupo pode existir 0 ou muitas vezes joao: | joao.silva

    # @ literal

    # \w+ depois do @ pode ter um o mais caracteres: email | outlook

    # colocando os mesmos caracteres especiaias depois do "gmail" -> para veridicar gmail.com hotmail.com.br
    # \w+ que pode haver algo depois do . ou -: ".com"

    # + pq pode ser repetido UMA ou Mais de uma vez: hotmail.com.br
    r'^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$',
      flags=re.M)


email_validator2 = re.compile(
    # ^$ padrão para buscar no começo ao fim da linha

    # [] para armazenar classe de caracteres
    # ^ -> se utilizado dentro dos colchetes = indica negação
    # \s indica espaço em branco
    # @<>()[] . proibindo esses caracteres no começo
    # + em cima dos colchetes para proibir 1 OU mais se for o caso

    # ?: para não captura do grupo, apenas para condicional e manipulação
    # . literal
    # # @<>()[] . proibindo esses caracteres se estiver concatenado com .
    # + em cima dos colchetes para proibir 1 OU mais se for o caso
    # * pode ter 0 ou mais desses caracteres ai

    # @ literal

    # [a-zA-Z0-9]+ verificando dps do @ se existe \w\d
    # + pode ter UMA ou MAIS no que tem no colchete

    # grupo de não captura, apenas de condicional
    # verificando de dps do "@" e do "gmail" existe . ou -
    # dps desse pondto deve haver \w\d, + pq pode se repetir UMA ou MAIS vezes
    # pode ter zero ou mais repetições nessa condicional

    # flags=re.M -> faz com que ^$ atuem no começo e final de cada linha

    r'^[^\s@<>\(\)\[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@[a-zA-Z0-9]+(?:[\.\-][a-zA-Z0-9]+)*$', flags=re.M
    )

# print(email_validator.findall(emails))
print(email_validator2.findall(emails))