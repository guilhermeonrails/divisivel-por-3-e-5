# coding=utf-8

def entrada_usuario():
    try:    
        entrada = int(input('Digite um número inteiro: '))
        return entrada
    except ValueError:
        print('Entrada inválida!')
    return entrada_usuario()