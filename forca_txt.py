import bisect
from time import sleep
from random import choice
import json
import os



catalogo = []


chaves = open("dicionario_csv.txt", "r").readline().strip().split(",")
#chaves = open("dicionario_csv.txt", encoding="utf8").readline().strip().split(",")

with open("dicionario_csv.txt", encoding="utf8") as palavras:
#with open("dicionario_csv.txt", "rb") as palavras:
    for palavra in palavras.readlines():
        # tratando a string, retirando espaços e caracteres especiais
        p = palavra.strip().replace("\t", "")
        # p = palavra.strip().replace(b"\t", b"")
        # quebrando os valores utilizando a vírgula como parâmetro
        p_as_list = p.split(",")
        # p_as_list = p.split(b",")
        # criando o dicionário com as chaves e os valores de cada item
        forca_dict = {}
        for valor in p_as_list:
            # adicionando ao dicionário 'forca_dict' a chave que você irá
            # ler em 'chaves' e o 'valor' que está no escopo deste loop for.
            if valor:
                forca_dict[chaves[p_as_list.index(valor)]] = valor
        # adicionando o dicionário 'forca_dict' à lista 'catalogo'
        catalogo.append(forca_dict)
        # dict.update(forca_dict)

# remove o primeiro item do catalogo
del catalogo[0]
print("====== Catalogo =====\n".center(30))

for palavra in catalogo:
    for coluna, valor in palavra.items():
        print("\t" + str(coluna) + " : " + str(valor))

    print("") # para gerar uma linha em branco entre os livros
    print("=-" * 15)

'''with open("catalogo.txt", "a") as arquivo:
    arquivo.write(str(catalogo))'''

numeros = [x for x in range(0, 80)]

def jogar():
    if len(numeros) == 0:
	    return print("Acabou o jogo!")
    palavra_acertadas = []
    letras_erradas = []
    erros = 0
    chances = 0

    with open("catalogo.txt", "r") as file:
        get = file.readlines()

        escolhido = choice(numeros)
        #key = frozenset(dict.items())

        palavra_secreta = str(get[escolhido][dict]['palavra'])

    for index in range(len(palavra_secreta)):
        palavra_acertadas.insert(index, '_')

    print(palavra_acertadas)

    while True:
        sleep(0.5)
        print()
        print(f"DICA: {get[escolhido]['dica']}")

        chute = input("Chute: ").upper()
        print()

        if chute.upper() == palavra_secreta.upper():
            print("Você ganhou!")
            break

        if chute in palavra_secreta.upper():
            if not chute in palavra_acertadas:
                print(f"TEM A LETRA [ {chute.upper()} ] NA PALAVRA SECRETA")

            for index, palavra in enumerate(palavra_secreta):
                if palavra.upper() == chute.upper():
                    palavra_acertadas[index] = chute

        else:
            erros += 1
            chances -= 1
            if not chute in letras_erradas:
                letras_erradas.append(chute)

        if not erros == 6:
            print(f"PALAVRA: {palavra_acertadas}")

        if erros == 6:
            print(f"Você perdeu, {palavra_secreta}")
            break

        if not '_' in palavra_acertadas:
            print("Ganhou")
            break

        print()
        print(f"Caracteres tentados: {letras_erradas}")

    numeros.remove(escolhido)

if __name__ == '__main__':
	while True:
		os.system('cls')
		jogar()
		print()
		jogar_dnv = input("Jogar denovo? [S/N] ").upper()
		if jogar_dnv  != 'S' or len(numeros) == 0:
			break










