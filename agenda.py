my_dict = {
    "pera": '123456',
    "maca": '234567',
    "kiwi": '345678',
    "uva": '456789',
    "manga": '567890',
    "abacaxi": '678901',
    "melao": '789012',
    "tomate": '890123',
    "banana": '901234',
    "laranja": '123457',
}
'''print(my_dict)'''
print("__________________________________")

# percorre o dicionário imprimindo os dados encontrados
'''print("Lista telefônica: ")
for key in my_dict.keys():
    print("%s: %s" %(key, my_dict[key]))'''

# funcão para retornar o valor onde a chave se inicia com a letra incerida pelo usuário
def lista_nome_input(my_dict):
    var = str(input("Insira a primeira letra do nome que deseja encontrar: "))
    for chave in my_dict.keys():
        if chave[0] == var.lower():
            print("%s: %s" %(chave, my_dict[chave]))
        else:
            pass

lista_nome_input(my_dict)

def lista_numero_input(my_dict):
    var_1 = str(input("Insira o primeiro número do telefone: "))
    var_2 = str(input("Insira o último número do telefone: "))
    for chave, valor in my_dict.items():
        if valor[0] == var_1 and valor[-1] == var_2:
            print("\n%s: %s" %(chave, valor))
        else:
            pass



lista_numero_input(my_dict)


