from calendar import isleap

anos = {}
count = 0

print("\nVALIDAÇÃO DE ANOS BISSEXTOS: ")
print("=============================\n")


while count < 5:
    indice = str(input("Insira o índice do ano: "))
    ano = str(input("Insira o ano: "))
    print("=============================")
    anos.update({"indice" + indice:ano})
    count += 1

print("Dicionário atual: ", anos)
print("=============================\n")

def validacao_ano_dic(anos):
        ano_input = input("Insira o ano que deseja validar: ")
        for valor in anos.values():
            if valor == ano_input:
                print("Ano encontrado.")
                print("=============================")
                if (int(ano_input) %4 == 0 and int(ano_input) % 100 != 0) or (int(ano_input) % 400 == 0):
                    print('Este ano é bissexto')
                else:
                    print('Este ano não é bissexto')
            else:
                print("-")

validacao_ano_dic(anos)













