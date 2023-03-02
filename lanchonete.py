lanches = {"1": "x-tudo", "2": "x-salada",
           "3": "x-bacon", "4": "x-egg",
            "5": "misto-quente"}

bebidas = {"1": "coca-cola", "2": "sprite",
           "3": "pepsi", "4": "guaraná",
           "5": "suco"}

sobremesas = {"1": "pudim", "2": "sorvete",
           "3": "pave", "4": "mousse",
           "5": "brigadeiro"}

pedido = []

pedido_list = []

#https://www.youtube.com/watch?v=-kcU29G6JHg&t=5s

print("===== Bem vindo ao restaurante! =====\n")

def print_lanches(lanches):
    for indice, lanche in lanches.items():
        print("=========-> LANCHES <-=========")
        print(f"--> Número do lanche: {indice}")
        print(f"--> Nome do lanche: {lanche}\n")
        # print("____________________________")

def print_bebidas(bebidas):
    for indice, bebida in bebidas.items():
        print("=========-> BEBIDAS <-=========")
        print(f"--> Número da bebida: {indice}")
        print(f"--> Nome da bebida: {bebida}\n")
        # print("____________________________")

def print_sobremesa(sobremesas):
    for indice, sobremesa in sobremesas.items():
        print("======== CARDÁPIO =======")
        print(f"-- Número da sobremesa: {indice}")
        print(f"Nome da sobremesa: {sobremesa}\n")
        # print("____________________________")

def escolha_lanches(lanches, pedido):
    print_lanches(lanches)
    print("____________________________")
    pedido_lanche = input("Qual o número do lanche que deseja pedir: \n")

    for numero_pedido in lanches.keys():

        if numero_pedido[0] == pedido_lanche.lower():
            print("Seu pedido é um: %s" % (lanches[numero_pedido]))
            var = ("%s:" "%s" % (numero_pedido, lanches[numero_pedido]))
            pedido.append(var)
            print("\n*********************************")

        else:
            pass

    print(f"Este é o seu pedido: {pedido}")
    escolha_bebida(bebidas, pedido)

def escolha_bebida(bebidas, pedido):
    print("*********************************\n")
    se_bebida = str(input("Deseja pedir uma bebida? (S/N)\n")).lower()

    if se_bebida == "s":
        print_bebidas(bebidas)
        print("_________________________________")
        pedido_bebida = input("Qual o número da bebida que deseja pedir: \n")

        for numero_pedido in bebidas.keys():

            if numero_pedido[0] == pedido_bebida.lower():
                print("Seu pedido é uma: %s" % (bebidas[numero_pedido]))
                var = ("%s:" "%s" % (numero_pedido, bebidas[numero_pedido]))
                pedido.append(var)
                print("\n*********************************")

            else:
                pass

        print(f"Este é o seu pedido: {pedido}")
        escolha_sobremesa(sobremesas, pedido)

    elif se_bebida == "n":
        finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)
    else:
        print("Valor incompreendido!")
        escolha_bebida(bebidas, pedido)

def escolha_sobremesa(sobremesas, pedido):
    print("*********************************\n")
    se_sobremesa = str(input("Deseja pedir uma sobremesa? (S/N)\n")).lower()

    if se_sobremesa == "s":
        print_sobremesa(sobremesas)
        print("_________________________________")
        pedido_sobremesa = input("Qual o número da sobremesa que deseja pedir:\n")

        for numero_pedido in sobremesas.keys():

            if numero_pedido[0] == pedido_sobremesa.lower():
                print("Seu pedido é uma: %s" % (sobremesas[numero_pedido]))
                var = ("%s:" "%s" % (numero_pedido, sobremesas[numero_pedido]))
                pedido.append(var)
                print("\n*********************************")

            else:
                pass

        print(f"Este é o seu pedido: {pedido}")
        finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)

    elif se_sobremesa == "n":
        finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)

    else:
        print("Valor incompreendido!")
        escolha_bebida(bebidas, pedido)

def finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list):
    print("*********************************\n\n")

    se_finalizar = str(input("Deseja finalizar o pedido: (S/N)\n")).lower()

    if se_finalizar == "s":
        print("____________________________")
        print("Seu pedido está sendo finalizado!")
        print("Confira o pedido abaixo: ")
        print(pedido[0])
        print(pedido[1])
        print(pedido[2])
        print(pedido)
        # print(pedido[3])
        correto = str(input("\nO pedido está correto? (S/N)\n")).lower()

        if correto == "s":
            print("____________________________")
            print("Pedido finalizado com sucesso!")
            print("A comanda está sendo gerada, logo mais entregue ao garçom!")
            # print(pedido)
            with open("comanda.txt", "a") as arquivo:
                arquivo.write(str(pedido))
                # lista_guardar = pedido_list.append(arquivo)
                # print(lista_guardar)

        elif correto == "n":
            print("____________________________")
            print("Realizade o pedido novamente.")
            escolha_lanches(lanches, pedido)

        else:
            print("____________________________")
            print("Valor incompreendido!")
            finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)

    elif se_finalizar == "n":
        se_pedido_dnv = str(input("Deseja pedir o que novamente: (lanche, bebida ou sobremesa): \n")).lower()
        if se_pedido_dnv == "lanche":
            escolha_lanches(lanches, pedido)
        elif se_pedido_dnv == "bebida":
            escolha_bebida(bebidas, pedido)
        elif se_pedido_dnv == "sobremesa":
            escolha_sobremesa(sobremesas, pedido)
        else:
            print("Valor incompreendido!")
            print("____________________________")
            finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)
    else:
        print("Valor incompreendido!")
        print("____________________________")
        finalizar_pedido(pedido, lanches, bebidas, sobremesas, pedido_list)

escolha_lanches(lanches, pedido)