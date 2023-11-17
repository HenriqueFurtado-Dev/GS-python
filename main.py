def menu():
    print("1 - Exibir usuarios")
    print("2 - Adicionar usuario")
    print("3 - Alterar usuario")
    print("4 - Ver informacoes de um usuario")
    print("5 - Ver procedimentos tecnicos")
    print("6 - Alterar estado")
    escolha_menu = int(input("Escolha uma opcao: "))

    return escolha_menu

def verificar_menu():
    escolha_menu = menu()
    if escolha_menu == 1:
        print("1")
    elif escolha_menu == 2:
        print("2")
    elif escolha_menu == 3:
        print("3")
    elif escolha_menu == 4:
        print("4")
    elif escolha_menu == 5:
        print("5")
    elif escolha_menu == 6:
        print("6")
    else: 
        print("Valor inválido")


def main():
    print("Seja bem vindo ao Gerenciador da SITREM")
    verificar_menu()

if __name__ == '__main__':
    main()