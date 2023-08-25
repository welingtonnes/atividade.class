lista_compras = []

def adicionar_item(item):
    lista_compras.append(item)
    print("Item adicionado à lista!")

def remover_item(item):
    if item in lista_compras:
        lista_compras.remove(item)
        print("Item removido da lista!")
    else:
        print("O item não está na lista.")

def editar_item(item_antigo, item_novo):
    if item_antigo in lista_compras:
        index = lista_compras.index(item_antigo)
        lista_compras[index] = item_novo
        print("Item editado!")
    else:
        print("O item não está na lista.")

def listar_itens():
    if len(lista_compras) > 0:
        print("Lista de Compras:")
        for item in lista_compras:
            print("- " + item)
    else:
        print("A lista de compras está vazia.")

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Editar item")
    print("4. Listar itens")
    print("5. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = input("Digite o nome do item: ")
        adicionar_item(item)
    elif opcao == 2:
        item = input("Digite o nome do item que deseja remover: ")
        remover_item(item)
    elif opcao == 3:
        item_antigo = input("Digite o nome do item que deseja editar: ")
        item_novo = input("Digite o novo nome do item: ")
        editar_item(item_antigo, item_novo)
    elif opcao == 4:
        listar_itens()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")