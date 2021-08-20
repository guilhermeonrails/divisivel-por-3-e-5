# Desafio Daniel 
> Faça um programa em Python que recebe um número inteiro, digitado pelo usuário, e apresentar uma mensagem:

`O número é divisível por 3 e 5`

- se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo.

- se o número que o usuário digitou não for divisível por 3 e por 5 ao mesmo tempo, exibir exibir a segunte mensagem:

`O número não é divisível por 3 e 5`

Segue abaixo a solução passo a passo deste programa..

## Faça um programa em Python

Podemos [instalar o Python](https://www.python.org/downloads/) em nosso SO e criar um arquivo `.py` para escrever nosso código Python ou podemos utilizar o [Colab](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=FQ_Hx_9tn7uF).

## Recebe um número inteiro

Para manter o código mais organizado, resolvi criar 2 arquivos: um para receber um número inteiro chamado **entrada.py** e outro para verificar se o número é divisível chamado de **app.py**.

No arquivo **entrada.py**, verifico se o valor da entrada do usuário é um número inteiro. Caso não seja, informo que a entrada é inválida e solicito uma nova entrada.

```
def entrada_usuario():
    try:    
        entrada = int(input('Digite um número inteiro: '))
        return entrada
    except ValueError:
        print('Entrada inválida!')
    return entrada_usuario()
```

## Verificando se é divisível por 3 e 5

No arquivo **app.py**, faço o import da função `entrada_usuário` .

```
from entrada import entrada_usuario
```

Por fim, crio uma função que verifica se o valor passado como argumento possui o `mod` de `3` igual a `0` **e** ao mesmo tempo se o o `mod` de `5` igual a `0`. 

Caso ambos sejam verdadeiros, retorno a mensagem informando que ambos são divisíveis. Caso contrário, informo que o valor não divisível por 3 e 5.

```
def verifica_divisivel(valor):
    if  valor % 3 == 0 and valor % 5 == 0:
        return print(f'{valor} é  divisível por 3 e 5')
    else:
        return print(f'{valor} não é divisível por 3 e 5')

verifica_divisivel(valor)
```
Daniel, espero que te ajude e boa sorte na sua jornada meu amigo!

**Gui Lima** 😊
