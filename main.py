from lib.interface import *
from time import sleep
from lib.archive import *

def main():

    arq = 'users.txt'

    if not arquivoExiste(arq):
        criarArquivo(arq)

    while True:
        resposta = menu(['Listar Usuários', 'Cadastrar Usuário', 'Sair do Sistema'])
        if resposta == 1:
            lerArquivo(arq)
        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = readInt('Idade: ')
            cadastrar(arq, nome, idade)
        elif resposta == 3:
            print('Saindo do Sistema... Até logo!')
            break
        else:
            print('\033[31mERRO! Por favor digite uma opção válida.\033[m')
        sleep(1.5)

main()