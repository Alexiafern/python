import os

def limpar_tela():
       os.system("cls")

def minha_funcao():
    return "Função do módulo"

if __name__ == '__main__':
        print('Este script está sendo executado sozinho!')
else:
        limpar_tela()
        print("Este script foi importado!")