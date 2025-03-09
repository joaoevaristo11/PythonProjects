print("------------------------")
print(f"{'MENU':^24}")  # Centraliza dentro de 24 caracteres
print("------------------------")

carrinho = {}

loja = {
    "banana": {"preço": 1.00, "stock": 30},
    "maçã": {"preço": 1.20, "stock": 20},
    "laranja": {"preço": 1.50, "stock": 10},
    "manga": {"preço": 3.00, "stock": 5},
    "cereja": {"preço": 0.20, "stock": 120},
    "morango": {"preço": 0.75, "stock": 30},
    "nêspera": {"preço": 0.80, "stock": 20},
    "pêra": {"preço": 1.00, "stock": 51},
}

def show_loja():
    print("\nProdutos disponíveis na loja:")
    for item, info in loja.items():
        print(f"{item.capitalize()} - {info['preço']}€ ({info['stock']} em stock)")
    print()

def show_carrinho():
    if not carrinho:
        print("\nO carrinho está vazio.")
    else:
        print("\nProdutos no carrinho:")
        for item, info in carrinho.items():
            print(f"{item.capitalize()} - {info['quantidade']} unidades ({info['preço']}€ cada)")
    print()

opcao = ""  # Inicializa a variável

while opcao != "5":
    opcao = input("\n1. Adicionar produto ao carrinho\n2. Remover produto do carrinho\n3. Listar produtos no carrinho\n4. Calcular total da compra\n5. Sair\n\nEscolha uma opção: ")
    
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Por favor digite uma das 5 opções...\n")
        continue

    if opcao == "1":
        show_loja()
        produto = input("Que produto pretende adicionar ao carrinho: ").lower()

        if produto in loja:
            quantidade = int(input("Qual a quantidade que pretende adquirir: "))

            if quantidade > loja[produto]["stock"]:
                print(f"Estoque insuficiente, só temos {loja[produto]['stock']} unidades.")
            else:
                # Adiciona ao carrinho
                if produto in carrinho:
                    carrinho[produto]["quantidade"] += quantidade
                else:
                    carrinho[produto] = {"preço": loja[produto]["preço"], "quantidade": quantidade}

                # Atualiza o stock
                loja[produto]["stock"] -= quantidade
                print(f"{quantidade} unidades de {produto} adicionadas ao carrinho!")

        else:
            print("Produto não encontrado.")

    elif opcao == "2":
        show_carrinho()
        produto = input("\nQue produto pretende remover do carrinho: ").lower()

        if produto in carrinho:
            del carrinho[produto]
            print(f"{produto.capitalize()} foi removido(a) com sucesso!")
        else:
            print("Produto não está no carrinho.")

    elif opcao == "3":
        show_carrinho()

    elif opcao == "4":
        total = 0
        for item, info in carrinho.items():
            total += info["preço"] * info["quantidade"]
        
        print(f"\nTotal da compra: {total:.2f}€")

    else:
        print("Saindo do programa...")
        break
