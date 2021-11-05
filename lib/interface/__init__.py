def readInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número na opção.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não digitar\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('\033[33mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    option = readInt('\033[32mSua opção: \033[m')
    return option