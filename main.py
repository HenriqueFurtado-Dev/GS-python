def menu():
    print("1 - Exibir usuarios")
    print("2 - Adicionar usuario")
    print("3 - Alterar usuario")
    print("4 - Ver informacoes de um usuario")
    print("5 - Ver procedimentos tecnicos")
    print("6 - Alterar estado")
    escolha_menu = input("Escolha uma opcao: ")

    return escolha_menu

def verificar_menu():
    print(escolha_menu)

def main():
    print("Seja bem vindo ao Gerenciador da SITREM")
    menu()
    verificar_menu()

if __name__ == '__main__':
    main()