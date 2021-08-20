from entrada import entrada_usuario

valor = entrada_usuario()

def verifica_divisivel(valor):
    if  valor % 3 == 0 and valor % 5 == 0:
        return print(f'{valor} é  divisível por 3 e 5')
    else:
        return print(f'{valor} não é divisível por 3 e 5')

verifica_divisivel(valor)

    